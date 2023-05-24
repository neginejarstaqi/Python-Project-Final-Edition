username = input("lotfan shomare daneshjooE khod ra vared konid:")
while username != ("1401230001"):
    print("shomare daneshjooE ghalat mibashad")
    username = input("lotfan shomare daneshjooE khod ra vared konid:")
print("shomare daneshjooE sahih mibashad")
password = input("lotfan Code melli khod ra varedkonid:")
while password != ("2081095025"):
    print("code melli ghalat ast")
    password = input("lotfan Code melli khod ra varedkonid")
print("code melli sahih mibashad")
print("khosh amadid")
emtiaz_player1 = 0
emtiaz_player2 = 0
while True :
    player_1 = input("lotfan entekhab konid : chap ya rast ?")
    player_1 = str.lower(player_1)
    if player_1 == "chap":
        print("player_1 : chap")
    elif player_1 == "rast":
        print("player_1 : rast ")
    else:
        print("entekhab shoma ghalat mibashad")
        player_1 = input("lotfan entekhab konid : chap ya rast ?")
    
    import random as rn
    randint = rn.randint(1 , 3)
    player_2 = randint
    if player_2 == 1:
        print("player_2 : chap")
    if player_2 ==2:
        print("player_2 : rast ")
    if player_1 == "chap" and player_2 == 1:
        print("barande : player_1")
        emtiaz_player1 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    elif player_1 == "chap" and player_2 == 2 :
        print("barande : player_2")
        emtiaz_player2 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    elif player_1 == "rast" and player_2 == 1 :
        print("barande : player_2")
        emtiaz_player2 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    elif player_1 == "rast" and player_2 == 2 :
        print("barande : player_1")
        emtiaz_player1 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    if emtiaz_player1 == 3 :
        print("Shoma barande shodid")
        break
    if emtiaz_player2 == 3 :
        print("Game Over")
        break