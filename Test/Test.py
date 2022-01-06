
from ntpath import join
from pyautocad import Autocad, APoint

def autocad_grid(x,y):

    acad = Autocad(create_if_not_exists=True)
    acad.prompt("Hello, Autocad from Python\n")
    print(acad.doc.Name)

# Mohamed Taouil
# grid maker
#main
    r_1 = APoint(0,0)
    r_2 = APoint(x,0)           #change these coords to change grid generator
    r_3 = APoint(x,y)
    r_4 = APoint(0,y)

#gang, pl = placeholder
    pl1= r_3[0]/2 -10
    pl2 = pl1 + 20
    r_5 = APoint(pl1,0)
    r_6 = APoint(pl1,r_3[1])
    r_7 = APoint(pl2, 0)
    r_8 = APoint(pl2, r_3[1])
#kamers
    ra = int(r_4[1]/100)
    rb = int(pl1/150)
    ty1 = ty2 = 100
    tx1 = tx2 = 150

#main
    acad.model.AddLine(r_1, r_2)
    acad.model.AddLine(r_2, r_3)
    acad.model.AddLine(r_3, r_4)
    acad.model.AddLine(r_4, r_1)
#gang
    acad.model.AddLine(r_5, r_6)
    acad.model.AddLine(r_7, r_8)
#kamers

#links
    for i in range(ra):
        r_9 = APoint(0,r_4[1]-ty1)
        r_10 = APoint(pl1,r_4[1]-ty1)
        acad.model.AddLine(r_9, r_10)
        ty1 += 100
    for i in range(rb):
        r_13 = APoint(pl1-tx1,r_4[1])
        r_14 = APoint(pl1-tx1,0)
        acad.model.AddLine(r_13, r_14)
        tx1 += 150

#rechts, 2 extra lijnen onder
    for i in range(ra):
        r_11 = APoint(pl2,r_4[1]-ty2)
        r_12 = APoint(r_3[0],r_4[1]-ty2)
        acad.model.AddLine(r_11, r_12)
        ty2 += 100

    for i in range(rb):
        r_15 = APoint(pl2+tx2,r_4[1])
        r_16 = APoint(pl2+tx2,0)
        acad.model.AddLine(r_15, r_16)
        tx2 += 150