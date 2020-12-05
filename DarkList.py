import os
from colorama import Fore
import time

print ( Fore.RED + """
                    [Welcome To Dark List]

▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀    ██▓     ██▓  ██████ ▄▄▄█████▓
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄    ▒██░    ░██░  ▒   ██▒░ ▓██▓ ░ 
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ░██████▒░██░▒██████▒▒  ▒██▒ ░ 
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░   ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░    
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░      ░ ░    ▒ ░░  ░  ░    ░      
   ░          ░  ░   ░     ░  ░          ░  ░ ░        ░           
 ░                                                                                 

                    Developer : Mr:Future
                
                    Thank's : Cipher 

""")
time.sleep(0.5)


filename = input(Fore.GREEN +"Enter a file name : "  )

name = input("Enter a first name : "  )

lastname = input("Enter a last name : "  )

nikname = input("Enter a Nick  name :"  )

city = input("Enter a City name : "  )

phone = input("Enter a phone number (11 numder) : "  )

brotherorsister = input("Enter a brother or sister or friend name :"  )

birthday = input("Birthday : "  )

list1 = []


if filename == "":
    filename = name


#////////////////////////////////////////////////////////////////////////////////////////////////////////


nametitle = name.title()

lastnametitle = lastname.title()

niknametitle = nikname.title()

citytitle = city.title()

brothertitle = brotherorsister.title()


#   title name for exploit

#//////////////////////////////////////////////////////////////////////////////////////////////////////////


neshan = ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","}","]","{","[","'",":","?","/",".",">","<",",","-_-","_-_","_-","-_"]

reves3_neshan = ['-_', '_-', '_-_', '-_-', ',', '<', '>', '.', '/', '?', ':', "'", '[', '{', ']', '}', '=', '+', '-', '_', ')', '(', '*', '&', '^', '%', '$', '#', '@', '!', '`', '~']

for i in neshan:
    list11 = str(name) + i + str(lastname)
    list1.append(list11)
    list12 = str(lastname) + i + str(name)
    list1.append(list12)
    list111 = str(name) + str(lastname)
    list1.append(list111)

    list1112 = str(lastname) + str(name)
    list1.append(list1112)
    


for b in neshan:
    list13 = str(name) + b + str(nikname)
    list1.append(list13)
    list14 = str(nikname) + b + str(name)
    list1.append(list14)
    list133 = str(name) + str(nikname)
    list1.append(list133)

    list133one = str(nikname) + str(name)
    list1.append(list133one)
    



for c in neshan:
    list15 = str(name) + c + str(city)
    list1.append(list15)
    list16 = str(city) + c + str(name)
    list1.append(list16)
    list166 = str(city) + str(name)
    list1.append(list166)

    list166one = str(name) + str(city)
    list1.append(list166one)
         



for d in neshan:
    list17 = str(name) + d + str(phone)
    list1.append(list17)
    list18 = str(phone) + d + str(name)
    list1.append(list18)
    list188 = str(phone) + str(name)
    list1.append(list188)

    list188one = str(name) + str(phone)
    list1.append(list188one)
    


for f in neshan:
    list19 = str(name) + f + str(brotherorsister)
    list1.append(list19)
    list20 = str(brotherorsister) + f + str(name)
    list1.append(list20)
    list200 = str(brotherorsister) + str(name)
    list1.append(list200)
      
    list200one = str(name) + str(brotherorsister)
    list1.append(list200one)


for g in neshan:
    list21 = str(name) + g + str(birthday)
    list1.append(list21)
    list22 = str(birthday) + g + str(name)
    list1.append(list22)
    list222 = str(birthday) + str(name)
    list1.append(list222)

    list222one = str(name) + str(birthday)
    list1.append(list222one)

#///////////////////////////////////////////////////////////////////////////////////////
#  nick name + birthday
for gnick in neshan:
    list21nick = str(nikname) + gnick + str(birthday)
    list1.append(list21nick)
    list22nicktwo = str(birthday) + gnick + str(nikname)
    list1.append(list22nicktwo)
    list222three = str(birthday) + str(nikname)
    list1.append(list222three)

    list222foo = str(nikname) + str(birthday)
    list1.append(list222foo)

#//////////////////////////////////////////////////////////////////////////////////////////
# nick name + phone
for phonenick in neshan:
    phonnick = str(nikname) + phonenick + str(phone)
    list1.append(phonnick)
    phonnick1 = str(phone) + phonenick + str(nikname)
    list1.append(phonnick1)
    phonnick3 = str(phone) + str(nikname)
    list1.append(phonnick3)

    phonnick4 = str(nikname) + str(phone)
    list1.append(phonnick4)

#//////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////
#name + lastname + birthday

# 1 2 3
for h in neshan:
    for h_reverse in reves3_neshan:
        list23 = str(name) + str(lastname) + str(birthday)
        list1.append(list23)
        list24 = str(name) + h + str(lastname) + str(birthday)
        list1.append(list24)
        list25 = str(name) +  str(lastname) + h +str(birthday)
        list1.append(list25)
        list26 = str(name) + h + str(lastname) + h_reverse +str(birthday)
        list1.append(list26)
        list266 = str(name) + h_reverse + str(lastname) + h +str(birthday)
        list1.append(list266)

#///////////////////////////////////////////////////////////////////////////////////
# 1 3 2
for ha in neshan:  
    for ha_revese in reves3_neshan: 
        list27 = str(name) + ha + str(birthday) + ha_revese +str(lastname)
        list1.append(list27)
        list277 = str(name) + ha_revese + str(birthday) + ha +str(lastname)
        list1.append(list277)
        list28 = str(name) + str(birthday) + ha +str(lastname)
        list1.append(list28)
        list29 = str(name) + ha + str(birthday) +str(lastname)
        list1.append(list29)
        list30 = str(name) + str(birthday) +str(lastname)
        list1.append(list30)

#//////////////////////////////////////////////////////////////////////////////////////
# 2 1 3
for hb in neshan:
    for hb_reverse in reves3_neshan:
        list31 = str(lastname) + hb + str(name) + hb_reverse +str(birthday)
        list1.append(list31)
        list311 = str(lastname) + hb_reverse + str(name) + hb +str(birthday)
        list1.append(list311)
        list32 = str(lastname) + str(name) + hb +str(birthday)
        list1.append(list32)
        list33 = str(lastname) + hb + str(name) +str(birthday)
        list1.append(list33)
        list34 = str(lastname) + str(name) + str(birthday)
        list1.append(list34)
#//////////////////////////////////////////////////////////////////////////////////////
# 2 3 1
for hc in neshan:    
    for hc_reverse in reves3_neshan:      
        list35 = str(lastname) + hc + str(birthday) + hc_reverse +str(name)
        list1.append(list35)
        list355 = str(lastname) + hc_reverse + str(birthday) + hc +str(name)
        list1.append(list355)
        list36 = str(lastname) + str(birthday) + hc +str(name)
        list1.append(list36)
        list37 = str(lastname) + hc + str(birthday) +str(name)
        list1.append(list37)
        list38 = str(lastname) + str(birthday) + str(name)
        list1.append(list38)

#//////////////////////////////////////////////////////////////////////////////////////
# 3 2 1
for hd in neshan:
    for hd_reverse in reves3_neshan:
        list39 = str(birthday) + hd + str(lastname) + hd_reverse +str(name)
        list1.append(list39)
        list399 = str(birthday) + hd_reverse + str(lastname) + hd +str(name)
        list1.append(list399)
        list40 = str(birthday) + str(lastname) + hd +str(name)
        list1.append(list40)
        list41 = str(birthday) + hd + str(lastname) +str(name)
        list1.append(list41)
        list42 = str(birthday) + str(lastname) + str(name)
        list1.append(list42)

 #//////////////////////////////////////////////////////////////////////////////////
 # 3 1 2
for he in neshan:
    for he_reverse in reves3_neshan:
        list43 = str(birthday) + he + str(name) + he_reverse +str(lastname)
        list1.append(list43)
        list433 = str(birthday) + he_reverse + str(name) + he +str(lastname)
        list1.append(list433)
        list44 = str(birthday) + str(name) + he +str(lastname)
        list1.append(list44)
        list45 = str(birthday) + he + str(name) +str(lastname)
        list1.append(list45)
        list46 = str(birthday) + str(name) + str(lastname)
        list1.append(list46)

# name +  user name +  nikname
# #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
########################################################################################################################

# name + lastname + phone

for nm in neshan:
    for nm_reverse in reves3_neshan:
        list47 = str(name) + nm + str(lastname) + nm_reverse +str(phone)
        list1.append(list47)
        list477 = str(name) + nm_reverse + str(lastname) + nm +str(phone)
        list1.append(list477)
        list48 = str(name) + str(lastname) + nm +str(phone)
        list1.append(list48)
        list49 = str(name) + nm + str(lastname) +str(phone)
        list1.append(list49)
        list50 = str(name) + str(lastname) +str(phone)
        list1.append(list50)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
for nmm in neshan:
    for nmm_reverse in reves3_neshan:
        list51 = str(name) + nmm + str(phone) + nmm_reverse +str(lastname)
        list1.append(list51)
        list511 = str(name) + nmm_reverse + str(phone) + nmm +str(lastname)
        list1.append(list511)
        list52 = str(name) + str(phone) + nmm +str(lastname)
        list1.append(list52)
        list53 = str(name) + nmm + str(phone) +str(lastname)
        list1.append(list53)
        list54 = str(name) + str(phone) +str(lastname)
        list1.append(list54)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
for nmmm in neshan:
    for nmmm_reverse in reves3_neshan:
        list55 = str(lastname) + nmmm + str(name) + nmmm_reverse +str(phone)
        list1.append(list55)
        list555 = str(lastname) + nmmm_reverse + str(name) + nmmm +str(phone)
        list1.append(list555)
        list56 = str(lastname) + str(name) + nmmm +str(phone)
        list1.append(list56)
        list57 = str(lastname) + nmmm + str(name) +str(phone)
        list1.append(list57)
        list58 = str(lastname) + str(name) +str(phone)
        list1.append(list58)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
for nmn in neshan:
    for nmn_reverse in reves3_neshan:
        list59 = str(lastname) + nmn + str(phone) + nmn_reverse +str(name)
        list1.append(list59)

        list599 = str(lastname) + nmn_reverse + str(phone) + nmn +str(name)
        list1.append(list599)

        list60 = str(lastname) + str(phone) + nmn +str(name)
        list1.append(list60)
        list61 = str(lastname) + nmn + str(phone) +str(name)
        list1.append(list61)
        list62 = str(lastname) + str(phone) +str(name)
        list1.append(list62)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
for nph in neshan:
    for nph_reverse in reves3_neshan:
        list64 = str(phone) + nph + str(lastname) + nph_reverse +str(name)
        list1.append(list64)

        list644 = str(phone) + nph_reverse + str(lastname) + nph +str(name)
        list1.append(list644)

        list65 = str(phone) + str(lastname) + nph +str(name)
        list1.append(list65)
        list66 = str(phone) + nph + str(lastname) +str(name)
        list1.append(list66)
        list67 = str(phone) + str(lastname) +str(name)
        list1.append(list67)  

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
for nend in neshan:
    for nph_reverse in reves3_neshan:
        list68 = str(phone) + nend + str(name) + nph_reverse +str(lastname)
        list1.append(list68)

        list688 = str(phone) + nph_reverse + str(name) + nend +str(lastname)
        list1.append(list688)

        list69 = str(phone) + str(name) + nend +str(lastname)
        list1.append(list69)
        list70 = str(phone) + nend + str(name) +str(lastname)
        list1.append(list70)
        list71 = str(phone) + str(name) +str(lastname)
        list1.append(list71) 


# name + lastname + phone


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# name + nick name + phone

# 1 2 3
for nam_nick in neshan:
    for nam_reverse in reves3_neshan:
        nam_phonick = str(name) + nam_nick + str(nikname) + nam_reverse +str(phone)
        list1.append(nam_phonick)
        nam_phonick1 = str(name) + nam_reverse + str(nikname) + nam_nick +str(phone)
        list1.append(nam_phonick1)
        nam_phonick2 = str(name) + str(nikname) + nam_nick +str(phone)
        list1.append(nam_phonick2)
        nam_phonick3 = str(name) + nam_nick + str(nikname) +str(phone)
        list1.append(nam_phonick3)
        nam_phonick4 = str(name) + str(nikname) +str(phone)
        list1.append(nam_phonick4) 
##########################################################################################
# 1 3 2
for nam_nick1 in neshan:
    for nam_reverse2 in reves3_neshan:
        nam_phonick5 = str(name) + nam_nick1 + str(phone) + nam_reverse2 +str(nikname)
        list1.append(nam_phonick5)
        nam_phonick6 = str(name) + nam_reverse2 + str(phone) + nam_nick1 +str(nikname)
        list1.append(nam_phonick6)
        nam_phonick7 = str(name) + str(phone) + nam_nick1 +str(nikname)
        list1.append(nam_phonick7)
        nam_phonick8 = str(name) + nam_nick1 + str(phone) +str(nikname)
        list1.append(nam_phonick8)
        nam_phonick9 = str(name) + str(phone) +str(nikname)
        list1.append(nam_phonick9) 
################################################################################################
# 2 1 3
for nam_nick2 in neshan:
    for nam_reverse3 in reves3_neshan:
        nam_phonick10 = str(nikname) + nam_nick2 + str(name) + nam_reverse3 +str(phone)
        list1.append(nam_phonick10)
        nam_phonick11 = str(nikname) + nam_reverse3 + str(name) + nam_nick2 +str(phone)
        list1.append(nam_phonick11)
        nam_phonick12 = str(nikname) + str(name) + nam_nick2 +str(phone)
        list1.append(nam_phonick12)
        nam_phonick13 = str(nikname) + nam_nick2 + str(name) +str(phone)
        list1.append(nam_phonick13)
        nam_phonick14 = str(nikname) + str(name) +str(phone)
        list1.append(nam_phonick14) 
################################################################################################
# 2 3 1

for nam_phonick3 in neshan:
    for nam_reverse4 in reves3_neshan:
        nam_phonick15 = str(nikname) + nam_phonick3 + str(phone) + nam_reverse4 +str(name)
        list1.append(nam_phonick15)
        nam_phonick16 = str(nikname) + nam_reverse4 + str(phone) + nam_phonick3 +str(name)
        list1.append(nam_phonick16)
        nam_phonick17 = str(nikname) + str(phone) + nam_phonick3 +str(name)
        list1.append(nam_phonick17)
        nam_phonick18 = str(nikname) + nam_phonick3 + str(phone) +str(name)
        list1.append(nam_phonick18)
        nam_phonick19 = str(nikname) + str(phone) +str(name)
        list1.append(nam_phonick19) 
#####################################################################################################
# 3 2 1
for nam_phonick4 in neshan:
    for nam_reverse5 in reves3_neshan:
        nam_phonick20 = str(phone) + nam_phonick4 + str(nikname) + nam_reverse5 +str(name)
        list1.append(nam_phonick20)
        nam_phonick21 = str(phone) + nam_reverse5 + str(nikname) + nam_phonick4 +str(name)
        list1.append(nam_phonick21)
        nam_phonick22 = str(phone) + str(nikname) + nam_phonick4 +str(name)
        list1.append(nam_phonick22)
        nam_phonick23 = str(phone) + nam_phonick4 + str(nikname) +str(name)
        list1.append(nam_phonick23)
        nam_phonick24 = str(phone) + str(nikname) +str(name)
        list1.append(nam_phonick24) 
########################################################################################################
# 3 1 2
for nam_phonick4 in neshan:
    for nam_reverse5 in reves3_neshan:
        nam_phonick205 = str(phone) + nam_phonick4 + str(name) + nam_reverse5 +str(nikname)
        list1.append(nam_phonick205)
        nam_phonick215 = str(phone) + nam_reverse5 + str(name) + nam_phonick4 +str(nikname)
        list1.append(nam_phonick215)
        nam_phonick225 = str(phone) + str(name) + nam_phonick4 +str(nikname)
        list1.append(nam_phonick225)
        nam_phonick235 = str(phone) + nam_phonick4 + str(name) +str(nikname)
        list1.append(nam_phonick235)
        nam_phonick245 = str(phone) + str(name) +str(nikname)
        list1.append(nam_phonick245) 


#////////////////////////////////////////////////////////////////////////////////////////////////////////
#========================================================================================================
# name + phone + city

# 1 2 3
for halat3 in neshan:
    for dovomi in reves3_neshan:
        three1 = str(name) + halat3 + str(phone) + dovomi +str(city)
        list1.append(three1)
        three2 = str(name) + dovomi + str(phone) + halat3 +str(city)
        list1.append(three2)
        three3 = str(name) + str(phone) + halat3 +str(city)
        list1.append(three3)
        three4 = str(name) + halat3 + str(phone) +str(city)
        list1.append(three4)
        three5 = str(name) + str(phone) +str(city)
        list1.append(three5) 

##########################################################################################

# 1 3 2

for halat31 in neshan:
    for dovomi1 in reves3_neshan:
        three6 = str(name) + halat31 + str(city) + dovomi1 +str(phone)
        list1.append(three6)
        three7 = str(name) + dovomi1 + str(city) + halat31 +str(phone)
        list1.append(three7)
        three8 = str(name) + str(city) + halat31 +str(phone)
        list1.append(three8)
        three9 = str(name) + halat31 + str(city) +str(phone)
        list1.append(three9)
        three10 = str(name) + str(city) +str(phone)
        list1.append(three10) 

################################################################################################
# 2 1 3
for halat32 in neshan:
    for dovomi2 in reves3_neshan:
        three11 = str(phone) + halat32 + str(name) + dovomi2 +str(city)
        list1.append(three11)
        three12 = str(phone) + dovomi2 + str(name) + halat32 +str(city)
        list1.append(three12)
        three13 = str(phone) + str(name) + halat32 +str(city)
        list1.append(three13)
        three14 = str(phone) + halat32 + str(name) +str(city)
        list1.append(three14)
        three15 = str(phone) + str(name) +str(city)
        list1.append(three15) 
################################################################################################
# 2 3 1

for halat33 in neshan:
    for dovomi3 in reves3_neshan:
        three111 = str(phone) + halat33 + str(city) + dovomi3 +str(name)
        list1.append(three111)
        three122 = str(phone) + dovomi3 + str(city) + halat33 +str(name)
        list1.append(three122)
        three133 = str(phone) + str(city) + halat33 +str(name)
        list1.append(three133)
        three144 = str(phone) + halat33 + str(city) +str(name)
        list1.append(three144)
        three155 = str(phone) + str(city) +str(name)
        list1.append(three155) 
#####################################################################################################
# 3 2 1
for halat34 in neshan:
    for dovomi4 in reves3_neshan:
        three1112 = str(city) + halat34 + str(phone) + dovomi4 +str(name)
        list1.append(three1112)
        three1113 = str(city) + dovomi4 + str(phone) + halat34 +str(name)
        list1.append(three1113)
        three11137 = str(city) + str(phone) + halat34 +str(name)
        list1.append(three11137)
        three1114 = str(city) + halat34 + str(phone) +str(name)
        list1.append(three1114)
        three1115 = str(city) + str(phone) +str(name)
        list1.append(three1115) 
########################################################################################################
# 3 1 2
for halat35 in neshan:
    for dovomi5 in reves3_neshan:
        nam_phonick205nik = str(city) + halat35 + str(name) + dovomi5 +str(phone)
        list1.append(nam_phonick205nik)
        nam_phonick215nik = str(city) + dovomi5 + str(name) + halat35 +str(phone)
        list1.append(nam_phonick215nik)
        nam_phonick225nik = str(city) + str(name) + halat35 +str(phone)
        list1.append(nam_phonick225nik)
        nam_phonick235nik = str(city) + halat35 + str(name) +str(phone)
        list1.append(nam_phonick235nik)
        nam_phonick245nik = str(city) + str(name) +str(phone)
        list1.append(nam_phonick245nik) 


#============================================================================================================
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# name + birthday + city

# 1 2 3

for final in neshan:
    for nambir in reves3_neshan:
        brit1 = str(name) + final + str(birthday) + nambir +str(city)
        list1.append(brit1)

        brit2 = str(name) + nambir + str(birthday) + final +str(city)
        list1.append(brit2)

        brit3 = str(name) + str(birthday) + final +str(city)
        list1.append(brit3)

        brit4 = str(name) + final + str(birthday) +str(city)
        list1.append(brit4)

        brit5 = str(name) + str(birthday) +str(city)
        list1.append(brit5) 

##########################################################################################

# 1 3 2

for finalone in neshan:
    for nambir2 in reves3_neshan:

        brit6 = str(name) + finalone + str(city) + nambir2 +str(birthday)
        list1.append(brit6)

        brit7 = str(name) + nambir2 + str(city) + finalone +str(birthday)
        list1.append(brit7)

        brit8 = str(name) + str(city) + finalone +str(birthday)
        list1.append(brit8)

        brit9 = str(name) + finalone + str(city) +str(birthday)
        list1.append(brit9)

        brit10 = str(name) + str(city) +str(birthday)
        list1.append(brit10) 

################################################################################################
# 2 1 3
# name + birthday + city

for finaltwo in neshan:
    for nambir3 in reves3_neshan:

        brit11 = str(birthday) + finaltwo + str(name) + nambir3 +str(city)
        list1.append(brit11)

        brit12 = str(birthday) + nambir3 + str(name) + finaltwo +str(city)
        list1.append(brit12)

        brit13 = str(birthday) + str(name) + finaltwo +str(city)
        list1.append(brit13)

        brit14 = str(birthday) + finaltwo + str(name) +str(city)
        list1.append(brit14)
        
        brit15 = str(birthday) + str(name) +str(city)
        list1.append(brit15) 

################################################################################################
# 2 3 1
# name + birthday + city

for final3t in neshan:
    for nambir4f in reves3_neshan:

        brit16 = str(birthday) + final3t + str(city) + nambir4f +str(name)
        list1.append(brit16)

        brit17 = str(birthday) + nambir4f + str(city) + final3t +str(name)
        list1.append(brit17)

        brit18 = str(birthday) + str(city) + final3t +str(name)
        list1.append(brit18)

        brit19 = str(birthday) + final3t + str(city) +str(name)
        list1.append(brit19)

        brit20 = str(birthday) + str(city) +str(name)
        list1.append(brit20) 
#####################################################################################################
# 3 2 1
# name + birthday + city

for final4fo in neshan:
    for nambir5fi in reves3_neshan:

        brit21 = str(city) + final4fo + str(birthday) + nambir5fi +str(name)
        list1.append(brit21)

        brit22 = str(city) + nambir5fi + str(birthday) + final4fo +str(name)
        list1.append(brit22)

        brit23 = str(city) + str(birthday) + final4fo +str(name)
        list1.append(brit23)

        brit24 = str(city) + final4fo + str(birthday) +str(name)
        list1.append(brit24)

        brit25 = str(city) + str(birthday) +str(name)
        list1.append(brit25) 

########################################################################################################
# 3 1 2
for finalendd in neshan:
    for ebded in reves3_neshan:

        brit256 = str(city) + finalendd + str(name) + ebded +str(birthday)
        list1.append(brit256)

        brit257 = str(city) + ebded + str(name) + finalendd +str(birthday)
        list1.append(brit257)

        brit258 = str(city) + str(name) + finalendd +str(birthday)
        list1.append(brit258)

        brit259 = str(city) + finalendd + str(name) +str(birthday)
        list1.append(brit259)

        brit250 = str(city) + str(name) +str(birthday)
        list1.append(brit250) 

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#******************************************************************************************************
# name + nickname + birthday
# 1 2 3

for groh in neshan:
    for ziro in reves3_neshan:

        gholi = str(name) + groh + str(nikname) + ziro +str(birthday)
        list1.append(gholi)

        gholi1 = str(name) + ziro + str(nikname) + groh +str(birthday)
        list1.append(gholi1)

        gholi2 = str(name) + str(nikname) + groh +str(birthday)
        list1.append(gholi2)

        gholi3 = str(name) + groh + str(nikname) +str(birthday)
        list1.append(gholi)

        gholi4 = str(name) + str(nikname) +str(birthday)
        list1.append(gholi4) 

##########################################################################################

# 1 3 2
# name + nickname + birthday

for groh1 in neshan:
    for ziro1 in reves3_neshan:

        gholi5 = str(name) + groh1 + str(birthday) + ziro1 +str(nikname)
        list1.append(gholi5)

        gholi6 = str(name) + ziro1 + str(birthday) + groh1 +str(nikname)
        list1.append(gholi6)

        gholi7 = str(name) + str(birthday) + groh1 +str(nikname)
        list1.append(gholi7)

        gholi8 = str(name) + groh1 + str(birthday) +str(nikname)
        list1.append(gholi8)

        gholi9 = str(name) + str(birthday) +str(nikname)
        list1.append(gholi9) 

################################################################################################
# 2 1 3
# name + nickname + birthday

for groh2 in neshan:
    for ziro2 in reves3_neshan:

        gholi10 = str(nikname) + groh2 + str(name) + ziro2 +str(birthday)
        list1.append(gholi10)

        gholi11 = str(nikname) + ziro2 + str(name) + groh2 +str(birthday)
        list1.append(gholi11)

        gholi12 = str(nikname) + str(name) + groh2 +str(birthday)
        list1.append(gholi12)

        gholi13 = str(nikname) + groh2 + str(name) +str(birthday)
        list1.append(gholi13)
        
        gholi14 = str(nikname) + str(name) +str(birthday)
        list1.append(gholi14) 

################################################################################################
# 2 3 1
# name + nickname + birthday

for groh3 in neshan:
    for ziro3 in reves3_neshan:

        gholi14 = str(nikname) + groh3 + str(birthday) + ziro3 +str(name)
        list1.append(gholi14)

        gholi15 = str(nikname) + ziro3 + str(birthday) + groh3 +str(name)
        list1.append(gholi15)

        gholi16 = str(nikname) + str(birthday) + groh3 +str(name)
        list1.append(gholi16)

        gholi17 = str(nikname) + groh3 + str(birthday) +str(name)
        list1.append(gholi17)

        gholi18 = str(nikname) + str(birthday) +str(name)
        list1.append(gholi18) 

#####################################################################################################
# 3 2 1
# name + nickname + birthday

for groh4 in neshan:
    for ziro4 in reves3_neshan:

        gholi19 = str(birthday) + groh4 + str(nikname) + ziro4 +str(name)
        list1.append(gholi19)

        gholi181 = str(birthday) + ziro4 + str(nikname) + groh4 +str(name)
        list1.append(gholi181)

        gholi182 = str(birthday) + str(nikname) + groh4 +str(name)
        list1.append(gholi182)

        gholi183 = str(birthday) + groh4 + str(nikname) +str(name)
        list1.append(gholi183)

        gholi184 = str(birthday) + str(nikname) +str(name)
        list1.append(gholi184) 

########################################################################################################
# 3 1 2
# name + nickname + birthday

for groh5 in neshan:
    for ziro5 in reves3_neshan:

        ennde2 = str(city) + groh5 + str(name) + ziro5 +str(birthday)
        list1.append(ennde2)

        ennde21 = str(city) + ziro5 + str(name) + groh5 +str(birthday)
        list1.append(ennde21)

        ennde22 = str(city) + str(name) + groh5 +str(birthday)
        list1.append(ennde22)

        ennde23 = str(city) + groh5 + str(name) +str(birthday)
        list1.append(ennde23)

        ennde24 = str(city) + str(name) +str(birthday)
        list1.append(ennde24) 

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# nikname + phone + city
# 1 2 3

for oneeend in neshan:
    for tamom in reves3_neshan:

        akhhbin = str(nikname) + oneeend + str(phone) + tamom +str(city)
        list1.append(akhhbin)

        akhhbin1 = str(nikname) + tamom + str(phone) + oneeend +str(city)
        list1.append(akhhbin1)

        akhhbin2 = str(nikname) + str(phone) + oneeend +str(city)
        list1.append(akhhbin2)

        akhhbin3 = str(nikname) + oneeend + str(phone) +str(city)
        list1.append(akhhbin3)

        akhhbin4 = str(nikname) + str(phone) +str(city)
        list1.append(akhhbin4) 

##########################################################################################

# 1 3 2
# nikname + phone + city

for oneeend1 in neshan:
    for tamom1 in reves3_neshan:

        akhhbin5 = str(nikname) + oneeend1 + str(city) + tamom1 +str(phone)
        list1.append(akhhbin5)

        akhhbin6 = str(nikname) + tamom1 + str(city) + oneeend1 +str(phone)
        list1.append(akhhbin6)

        akhhbin7 = str(nikname) + str(city) + oneeend1 +str(phone)
        list1.append(akhhbin7)

        akhhbin8 = str(nikname) + oneeend1 + str(city) +str(phone)
        list1.append(akhhbin8)

        akhhbin9 = str(nikname) + str(city) +str(phone)
        list1.append(akhhbin9) 

################################################################################################
# 2 1 3
# nikname + phone + city

for oneeend2 in neshan:
    for tamom2 in reves3_neshan:

        akhhbin10 = str(phone) + oneeend2 + str(nikname) + tamom2 +str(city)
        list1.append(akhhbin10)

        akhhbin11 = str(phone) + tamom2 + str(nikname) + oneeend2 +str(city)
        list1.append(akhhbin11)

        akhhbin12 = str(phone) + str(nikname) + oneeend2 +str(city)
        list1.append(akhhbin12)

        akhhbin13 = str(phone) + oneeend2 + str(nikname) +str(city)
        list1.append(akhhbin13)
        
        akhhbin14 = str(phone) + str(nikname) +str(city)
        list1.append(akhhbin14) 

################################################################################################
# 2 3 1
# nikname + phone + city

for oneeend3 in neshan:
    for tamom3 in reves3_neshan:

        akhhbin15 = str(phone) + oneeend3 + str(city) + tamom3 +str(nikname)
        list1.append(akhhbin15)

        akhhbin16 = str(phone) + tamom3 + str(city) + oneeend3 +str(nikname)
        list1.append(akhhbin16)

        akhhbin17 = str(phone) + str(city) + oneeend3 +str(nikname)
        list1.append(akhhbin17)

        akhhbin18 = str(phone) + oneeend3 + str(city) +str(nikname)
        list1.append(akhhbin18)

        akhhbin19 = str(phone) + str(city) +str(nikname)
        list1.append(akhhbin19) 

#####################################################################################################
# 3 2 1
# nikname + phone + city

for oneeend4 in neshan:
    for tamom4 in reves3_neshan:

        akhhbin20 = str(city) + oneeend4 + str(phone) + tamom4 +str(nikname)
        list1.append(akhhbin20)

        akhhbin21 = str(city) + tamom4 + str(phone) + oneeend4 +str(nikname)
        list1.append(akhhbin21)

        akhhbin22 = str(city) + str(phone) + oneeend4 +str(nikname)
        list1.append(akhhbin22)

        akhhbin23 = str(city) + oneeend4 + str(phone) +str(nikname)
        list1.append(akhhbin23)

        akhhbin24 = str(city) + str(phone) +str(nikname)
        list1.append(akhhbin24) 

########################################################################################################
# 3 1 2

# nikname + phone + city

for oneeend5 in neshan:
    for tamom4 in reves3_neshan:

        akhhbin241 = str(city) + oneeend5 + str(nikname) + tamom4 +str(phone)
        list1.append(akhhbin241)

        akhhbin242 = str(city) + tamom4 + str(nikname) + oneeend5 +str(phone)
        list1.append(akhhbin242)

        akhhbin243 = str(city) + str(nikname) + oneeend5 +str(phone)
        list1.append(akhhbin243)

        akhhbin244 = str(city) + oneeend5 + str(nikname) +str(phone)
        list1.append(akhhbin244)

        akhhbin245 = str(city) + str(nikname) +str(phone)
        list1.append(akhhbin245) 

#   title name for exploit

for tit in neshan:

    nmtitone = str(nametitle) + tit + str(lastnametitle)
    list1.append(nmtitone)

    nmtittwo = str(lastnametitle) + tit + str(nametitle)
    list1.append(nmtittwo)

    nmtitthre = str(nametitle)  + tit + str(lastname)
    list1.append(nmtitthre)

    nmtitfo = str(lastnametitle)  + tit + str(name)
    list1.append(nmtitfo)

    nmtitfive = str(name)  + tit + str(lastnametitle)
    list1.append(nmtitfive)

    nmtitsix = str(lastname)  + tit + str(nametitle)
    list1.append(nmtitsix)


for tittwo in neshan:

    nick1 = str(nametitle) + tittwo + str(niknametitle)
    list1.append(nick1)

    nick2 = str(niknametitle) + tittwo + str(nametitle)
    list1.append(nick2)

    nick3 = str(nametitle)  + tittwo + str(nikname)
    list1.append(nick3)

    nick4 = str(niknametitle)  + tittwo + str(name)
    list1.append(nick4)

    nick5 = str(nikname)  + tittwo + str(nametitle)
    list1.append(nick5)

    nick6 = str(name)  + tittwo + str(niknametitle)
    list1.append(nick6)


list1 = list1
print(len(list1))

print(Fore.BLUE  + "Passwords Generate")

foooooj = open(filename+".txt","a")
for writ in list1:
    foooooj.write(str(writ) + "\n")







