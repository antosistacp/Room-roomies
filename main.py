from functions_one import *
data_base= dict() #ONLY RAN AT THE BEGINNING OF THE APP
weights = dict()
print("\nWELCOME TO THE ROOM&ROOMIES OFFICIAL PAGE\n")
user_name=False
data_base={'anto': [0.75, 1.2, 0, 1.4, 1.5333333333333334], 'garris': [2.25, 1.3599999999999999, 0.55, 0, 0], 'pilar': [2, 1.399, 0.7, 2, 1],'zhen': [2.25, 0, 0.55, 4, 1.1], 'valeria': [0, 3, 1.55, 0, 0.3]}
weights={'anto': [0.75, 1.2, 0, 1.4, 1.5333333333333334], 'garris': [2.25, 1.3599999999999999, 0.55, 0, 0], 'pilar': [2, 1.399, 0.7, 2, 1],'zhen': [2.25, 0, 0.55, 4, 1.1], 'valeria': [0, 3, 1.55, 0, 0.3]}

while True:
    if user_name==False:
        what1=input("What do you want to do?\n1.Log in \n2.Sign up\n\n")
        if what1 == "1":
            user_name=login(data_base,weights)
        else:
            user_name=signup(data_base,weights)
    else:
        what2=int(input("\nWhat do you want to do? \n1.Change user \n2.Assign my importance to the categories \n3.Score the questions \n4.See my matches\n5. Sign off\n\n"))
        if what2 == 1:
            user_name=False
        elif what2==2:
            weights=categories(user_name,weights)
            print("\nNOW YOU HAVE TO SCORE THE QUESTIONS!\n")
            data_base=questions(weights,data_base,user_name)
        elif what2==3:
            data_base=questions(weights,data_base,user_name)
        elif what2==4:
            a=matches(user_name,data_base)
        elif what2==5:
            print("See you next time!\n")
            break