#lets go 

nomber_0 = 0 
nomber_1 = 0
nomber_2 = 0
nomber_3 = 0
nomber_4 = 0
glav_masiv = []

While = 0 

while While == 0 : 
    nomber_0 = int(input("nomber here: "))
    nomber_1 = int(input("nomber_1 here : "))
    nomber_2 = int(input("nomber_2 here : "))
    nomber_3 = int(input("nomber_3 here : "))
    nomber_4 = int(input("nomber_4 here : "))
    glav_masiv = [nomber_0,nomber_1,nomber_2,nomber_3,nomber_4]
    if nomber_0 == 4 : 
        print("jump on 4 nomber")
    if nomber_0 >= 3 and nomber_3 >= 1 : 
        print("jump on 3 nomber and jump on nomber 4")
    if nomber_0 >= 2 and nomber_2 >= 2 : 
        print("jump on nomber 2 and jump on nomber 4 ")         #nomber_0 
    if nomber_0 >= 1 and nomber_1 >= 3 : 
        print("jump on nomber 1 and jump on nomber 4 ")
    if nomber_0 == 0 :
        print("u lose , sorry")
