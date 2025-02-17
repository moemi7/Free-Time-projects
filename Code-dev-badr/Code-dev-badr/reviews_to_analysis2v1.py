import os
from textblob import TextBlob
import pandas as pd
from utils import (
    order_csv_files,
    order_csv_filesyt,
    append_df,
    append_df_nodate,
    keyword_in_review,
    first_date_before_second_date,
)
from cleantext import clean
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import wordnet

#
def get_synonyms(words):
    all_synonyms = []
    for word in words:
        synonyms = []

        # Retrieve synsets for the word
        synsets = wordnet.synsets(word)
        # Extract synonyms from synsets
        for synset in synsets:
            for lemma in synset.lemmas():
                synonym = lemma.name()
                if synonym != word:
                    synonyms.append(synonym)

        # Remove duplicates and sort the synonyms
        synonyms = sorted(list(set(synonyms)))
        all_synonyms.extend(synonyms)
    all_synonyms.extend(words)
    return all_synonyms


def synonym_related(review_keywords, synonyms_list):
    for i in synonyms_list:
        for j in review_keywords:
            if i == j:
                return True
    return False


def get_reviews_by_keyword(keywords, df_reviews):
    list_synonyms = []
    first_synonyms = get_synonyms(keywords)
    list_synonyms = first_synonyms
    df_containing_keywords = df_reviews[
        df_reviews["keywords"].apply(lambda x: synonym_related(x, list_synonyms))
    ]
    return df_containing_keywords


def sentiment_analysis(review):
    sentiment = TextBlob(review).sentiment.polarity
    return sentiment


def keywords_positive_negative_time(keywords, df_reviews, time_start, time_end):
    greater_than_zero = pd.DataFrame()
    less_than_zero = pd.DataFrame()
    is_zero = pd.DataFrame()
    for i in keywords:
        greater_than_zero = pd.concat(
            [
                greater_than_zero,
                df_reviews[
                    (df_reviews["sentiment_polarity"] >= 0)
                    & (df_reviews["content"].str.contains(i, case=False))
                ],
            ]
        )
        less_than_zero = pd.concat(
            [
                less_than_zero,
                df_reviews[
                    (df_reviews["sentiment_polarity"] < 0)
                    & (df_reviews["content"].str.contains(i, case=False))
                ],
            ]
        )
        is_zero = pd.concat(
            [
                is_zero,
                df_reviews[
                    (df_reviews["sentiment_polarity"] == 0)
                    & (df_reviews["content"].str.contains(i, case=False))
                ],
            ]
        )

    greater_than_zero_counts = (
        greater_than_zero.groupby(["days"]).size().rename("num_positive_reviews")
    )
    less_than_zero_counts = (
        less_than_zero.groupby(["days"]).size().rename("num_negative_reviews")
    )
    is_zero = is_zero.groupby(["days"]).size().rename("num_neutral_reviews")
    result_df = pd.merge(
        greater_than_zero_counts,
        less_than_zero_counts,
        how="outer",
        left_index=True,
        right_index=True,
    )
    result_df = pd.merge(
        result_df, is_zero, how="outer", left_index=True, right_index=True
    )
    result_df.fillna(0, inplace=True)  # Fill NaN values with 0
    result_df.reset_index(inplace=True)
    result_df = result_df[
        result_df["days"].apply(lambda x: first_date_before_second_date(time_start, x))
        & result_df["days"].apply(lambda x: first_date_before_second_date(x, time_end))
    ]
    return result_df


def keyword_extraction(review):
    keywords = []

    # Single-word keywords
    vectorizer_single = CountVectorizer(ngram_range=(1, 1))
    try:
        review_matrix_single = vectorizer_single.fit_transform([review])
    except:
        return keywords
    single_keywords = vectorizer_single.get_feature_names_out()
    keywords.extend(single_keywords)

    # Bi-gram keywords
    vectorizer_bi = CountVectorizer(ngram_range=(2, 2))
    try:
        review_matrix_bi = vectorizer_bi.fit_transform([review])
    except:
        return keywords
    bi_gram_keywords = vectorizer_bi.get_feature_names_out()
    keywords.extend(bi_gram_keywords)

    return keywords


def analyze_dataframe(df_reviews):
    df_reviews = df_reviews.sort_index()

    df_reviews["days"] = df_reviews["at"].transform(lambda x: x.split(" ")[0])
    df_reviews = df_reviews.set_index(df_reviews["at"].rename("index"))

    df_reviews["content"] = df_reviews["content"].transform(
        lambda x: clean(x, no_emoji=True)
    )

    df_reviews.dropna(subset=["content"], inplace=True)

    df_reviews = df_reviews.sort_index()

    df_reviews["sentiment_polarity"] = df_reviews["content"].transform(
        lambda x: sentiment_analysis(str(x))
    )

    df_reviews["keywords"] = df_reviews["content"].transform(
        lambda x: keyword_extraction(x)
    )

    df_reviews = df_reviews.drop(
        df_reviews[df_reviews["keywords"].apply(lambda x: len(x) == 0)].index
    )
    return df_reviews

def analyze_dataframe_yt(df_comments):
    df_comments = df_comments.sort_index()
 
   # df_comments["days"] = df_comments["at"].transform(lambda x: x.split(" ")[0])
   # df_comments = df_comments.set_index(df_comments["at"].rename("index"))
    print(df_comments)

    df_comments["comment"] = df_comments["comment"].transform(
        lambda x: clean(x, no_emoji=True)
    )

    df_comments.dropna(subset=["comment"], inplace=True)

    df_comments = df_comments.sort_index()

    df_comments["sentiment_polarity"] = df_comments["comment"].transform(
        lambda x: sentiment_analysis(str(x))
    )

    df_comments["keywords"] = df_comments["comment"].transform(
        lambda x: keyword_extraction(x)
    )

    df_comments = df_comments.drop(
        df_comments[df_comments["keywords"].apply(lambda x: len(x) == 0)].index
    )
    return df_comments

def analyze_reviews(app_name,directory):
    folder_path = os.path.join("saved_dataframes", app_name)
    df_saved = pd.DataFrame()
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]
    if csv_files:
        df_saved = append_df(folder_path, csv_files)
    else:
        print("No csv files found")

    # directory = "Data/{}".format(app_name)
    #directory = os.path.join("Data", app_name)
    arr_files = order_csv_files(directory, descending=False)
    df_reviews = append_df(directory, arr_files)
    if not df_saved.empty:
        common_rows = df_reviews[df_reviews["reviewId"].isin(df_saved["reviewId"])]#######
        if not common_rows.empty:
            df_reviews = df_reviews[~df_reviews["reviewId"].isin(df_saved["reviewId"])]
            df_reviews = analyze_dataframe(df_reviews)
            df_reviews = pd.concat([df_reviews, common_rows], axis=0)
            df_reviews = df_reviews.sort_index()

        else:
            df_reviews = analyze_dataframe(df_reviews)
            df_reviews = df_reviews.sort_index()
    else:
        df_reviews = analyze_dataframe(df_reviews)
        df_reviews = df_reviews.sort_index()

    file_name = str(
        str(df_reviews["days"].iloc[0])
        + "_"
        + str(df_reviews["days"].iloc[-1])
        + ".csv"
    )
    df_reviews.to_csv(
        os.path.join(folder_path, file_name), encoding="utf-8", index=False
    )
    return df_reviews
##################\


########
def analyze_reviews_nodate(yout_name,directory_y):
    folder_path = os.path.join("saved_dataframes", yout_name)
    df_saved = pd.DataFrame()
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    #csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]
   # if csv_files:
   #     print(csv_files)
   #     df_saved = append_df_nodate(folder_path, csv_files)
    #    print(df_saved)
    #else:
    #    print("No csv files found")

    # directory = "Data/{}".format(app_name)
    #directory = os.path.join("Data", app_name)
    #arr_files = order_csv_filesyt(directory_y, descending=False)
    #df_comments = pd.DataFrame()#append_df_nodate(directory_y, csv_files)
    print(folder_path)
    pat = folder_path + '\comments.csv'
    print(pat)
    df_comments = pd.read_csv(pat, encoding='latin1')  
    print(df_comments)
    if not df_saved.empty:
        common_rows = [df_comments["comment"].isin(df_saved["comment"])]
        if not common_rows.empty:
            df_comments = df_comments[~df_comments["comment"].isin(df_saved["comment"])]
            df_comments = analyze_dataframe_yt(df_comments)
            df_comments = pd.concat([df_comments, common_rows], axis=0)
            df_comments = df_comments.sort_index()

        else:
            df_comments = analyze_dataframe_yt(df_comments)
            df_comments = df_comments.sort_index()
    else:
        df_comments = analyze_dataframe_yt(df_comments)
        df_comments = df_comments.sort_index()

    file_name = 'comments.csv'
    df_comments.to_csv(
        os.path.join(folder_path, file_name), encoding="utf-8", index=False
    )
    return df_comments

###############
def get_reviews(df_reviews, keywords, time_start, time_end):
    return df_reviews[
        df_reviews["content"].apply(lambda x: keyword_in_review(keywords, x))
        & df_reviews["days"].apply(
            lambda x: first_date_before_second_date(time_start, x)
        )
        & df_reviews["days"].apply(lambda x: first_date_before_second_date(x, time_end))
    ]


def get_keywords_dict(df_reviews, time_start, time_end):
    positive_keywords_dict = {}
    negative_keywords_dict = {}
    neutral_keywords_dict = {}
    df_reviews_in_time = df_reviews[
        df_reviews["days"].apply(lambda x: first_date_before_second_date(time_start, x))
        & df_reviews["days"].apply(lambda x: first_date_before_second_date(x, time_end))
    ]
    for i in range(len(df_reviews_in_time)):
        for j in df_reviews_in_time["keywords"][i]:
            if df_reviews_in_time["sentiment_polarity"][i] > 0:
                if j in positive_keywords_dict:
                    positive_keywords_dict[j] += 1
                else:
                    positive_keywords_dict[j] = 1
            elif df_reviews_in_time["sentiment_polarity"][i] < 0:
                if j in negative_keywords_dict:
                    negative_keywords_dict[j] += 1
                else:
                    negative_keywords_dict[j] = 1
            elif df_reviews_in_time["sentiment_polarity"][i] == 0:
                if j in neutral_keywords_dict:
                    neutral_keywords_dict[j] += 1
                else:
                    neutral_keywords_dict[j] = 1

    return (positive_keywords_dict, negative_keywords_dict, neutral_keywords_dict)

######################
def get_keywords_dictnodate(df_reviews):
    positive_keywords_dict = {}
    negative_keywords_dict = {}
    neutral_keywords_dict = {}
    df_reviews_in_time = df_reviews[
        df_reviews["days"].apply(lambda x: first_date_before_second_date(time_start, x))
        & df_reviews["days"].apply(lambda x: first_date_before_second_date(x, time_end))
    ]
    for i in range(len(df_reviews_in_time)):
        for j in df_reviews_in_time["keywords"][i]:
            if df_reviews_in_time["sentiment_polarity"][i] > 0:
                if j in positive_keywords_dict:
                    positive_keywords_dict[j] += 1
                else:
                    positive_keywords_dict[j] = 1
            elif df_reviews_in_time["sentiment_polarity"][i] < 0:
                if j in negative_keywords_dict:
                    negative_keywords_dict[j] += 1
                else:
                    negative_keywords_dict[j] = 1
            elif df_reviews_in_time["sentiment_polarity"][i] == 0:
                if j in neutral_keywords_dict:
                    neutral_keywords_dict[j] += 1
                else:
                    neutral_keywords_dict[j] = 1

    return (positive_keywords_dict, negative_keywords_dict, neutral_keywords_dict)


def get_positive_negative_neutral_percentage(df_reviews):
    negative_percentage = len(df_reviews[df_reviews["sentiment_polarity"] < 0]) / len(
        df_reviews
    )
    neutral_percentage = len(df_reviews[df_reviews["sentiment_polarity"] == 0]) / len(
        df_reviews
    )
    positive_percentage = len(df_reviews[df_reviews["sentiment_polarity"] > 0]) / len(
        df_reviews
    )
    return (
        positive_percentage * 100,
        negative_percentage * 100,
        neutral_percentage * 100,
    )
