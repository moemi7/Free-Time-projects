import math



def q_last():
    opw1 = opw2 = 0
    lengte = 10
    q = 100
    begq, eindq = 5,8
    ql = (eindq-begq) * q
    aangrijppunt = (eindq+begq)/2
    qlastma = aangrijppunt * ql
    opw2 = qlastma/lengte
    opw1 = ql-opw2
    print(opw1,opw2)

q_last()