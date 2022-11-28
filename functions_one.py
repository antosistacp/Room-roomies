import statistics
import numpy as np
import pandas as pd
import random

def initialize(data_base,user_name):
    #needed for loop cause of sth i changed ask me if you want
    for i in range(0,5):
        data_base[user_name].append("")


#Fuction to sign up
def signup(data_base,weights):
    user_name = input("Create username: ")
    if user_name in data_base.keys():
        while user_name in data_base.keys():
            a=input("This username is already registered, you want to log in? (yes/no) ")
            if a=="yes":
                login(data_base,weights)
                return user_name
            elif a=="no":
                signup(data_base,weights)
                return user_name
    else:
        data_base[user_name] = []
        weights[user_name] = []
        initialize(data_base,user_name)
        print(f"{user_name} has been correctly created and logged in. Welcome to Room&Roomies!\n")
        return user_name

#Fuction to log in    
def login(data_base,weights):
    user_name = input("Username: ")
    if user_name not in data_base.keys():
        while user_name not in data_base.keys():
            a=input("This username is not registered, you want to sign up? (yes/no) ")
            if a=="yes":
                signup(data_base,weights)
            elif a=="no":
                login(data_base,weights)
    else:
        #data_base[user_name] = []
        #weights[user_name] = []
        print(f"{user_name} has been correctly logged in. Welcome back to Room&Roomies!\n")
    return user_name

#Fuction to assign the importance of each category
def categories(user_name,weights):
    questions=["Points awarded to your future roomate demographic characteristics: ","Points awarded to personality traits: ","Points awarded to schedules: ","Points awarded to house chores: ","Points awarded to forms of entertainment: "]
    username_weights=[]
    while sum(username_weights) != 10:
        print("You are awarded with 10 points, which can be distributed between the following categories. \nThe more points you award to a category, the most important we will consider it on your search. \nFollowing these instructions, please distribute 10 points across the following categories using integers.\n")
        points_available=10
        points_awarded=0
        username_weights=[]

        for question in questions:
            if points_available!=0:
                points_awarded = input(f"{question}")
                if points_awarded == "":
                    points_awarded=0
                points_awarded=int(points_awarded)    
                points_remaining=points_available
                points_available-=points_awarded

                while points_available<0:
                    print("You exceeded the number of points available")
                    print(f"You have {points_remaining} points left")
                    points_awarded = int(input(f"{question}"))
                    points_available=points_remaining-points_awarded
                    
                username_weights.append(points_awarded)
                if points_available != 0:
                    print(f"You have {points_available} points left")
                else:
                    print("No points left!")
            else:
                username_weights.append(0)
        print(f"\n{username_weights}\n")
        if sum(username_weights) != 10:
            print("You have to assign the 10 points, you can't leave any out!\n")

    weights[user_name] = username_weights
    weights
    return weights


#Fuction to assign the importance of each question
def questions(weights,data_base,user_name):
    def enter(puntuation):
        if puntuation=="":
            puntuation=0
        return int(puntuation)

    print ("Are you ready to find your perfect match? \nLet us get to know you! \n3, 2, 1, GOO!!")
    print("Rate from 1 to 10 how much you relate to the each of the following sentences. 1 being you don't relate with it at all and 10 being I completely relate")

    #Demograpics
    demographics = ["I prefer to live with people of my same ethnicity","I prefer to live with people with similar age as mine", "I prefer to live with people with my same gender", "I prefer to live people who is single"]
    user_demographics = []
    if weights[user_name][0] != 0:
        for demography in demographics:
            puntuation = input(f"{demography}: ")
            puntuation = enter(puntuation)
            while puntuation > 11 or puntuation < 1:
                puntuation = input(f"Rate from 1 to 10. {demography}: ")
                puntuation = enter(puntuation)

            user_demographics.append(puntuation)
        data_base[user_name][0]=weights[user_name][0]*statistics.mean(user_demographics)/10

    else:
        data_base[user_name][0]=0
    
    print("\n")
    
    #Psychographics
    personality_traits = ["I am social and extroverted","I don't like to spend time alone", "I am a loud person", "I am very methodic and organized", "I care a lot about my grades"]
    user_personality = []
    if weights[user_name][1] != 0:
        for personality in personality_traits:
            puntuation = input(f"{personality}: ")
            puntuation = enter(puntuation)
            while puntuation > 11 or puntuation < 1:
                puntuation = input(f"Rate from 1 to 10. {personality}: ")
                puntuation = enter(puntuation)
            user_personality.append(puntuation)
        data_base[user_name][1]=weights[user_name][1]*statistics.mean(user_personality)/10

    else:
        data_base[user_name][1]=0

    print("\n")

    #Schedules
    schedules = ["I wake up between 6am and 8am","I go to bed after 00:30am", "I shower in the mornings", "I have very strict and established eating schedules"]
    user_schedules = []
    if weights[user_name][2] != 0:
        for schedule in schedules:
            puntuation = input(f"{schedule}: ")
            puntuation = enter(puntuation)
            while puntuation > 11 or puntuation < 1:
                puntuation = input(f"Rate from 1 to 10. {schedule}: ")
                puntuation = enter(puntuation)
            user_schedules.append(puntuation)

        data_base[user_name][2]=weights[user_name][2]*statistics.mean(user_schedules)/10

    else:
        data_base[user_name][2]=0

    print("\n")
        
    #House chores
    chores = ["I leave the kitchen clean everytime I cook","I clean my room once a week", "I like making sure the house is tidy", "I am willing to do chores in common areas once a week"]
    user_chores = []
    if weights[user_name][3] != 0:
        for chore in chores:
            puntuation = input(f"{chore}: ")
            puntuation = enter(puntuation)
            while puntuation > 11 or puntuation < 1:
                puntuation = input(f"Rate from 1 to 10. {chore}: ")
                puntuation = enter(puntuation)
            user_chores.append(puntuation)
        
        data_base[user_name][3]= weights[user_name][3]*statistics.mean(user_chores)/10

    else:
        data_base[user_name][3]=0
    
    print("\n")

    #Entertainment
    entertainments = ["I often go to clubs","I enjoy arts in general, such as reading and painting", "I like to watch series and movies","I like to spend my freetime out", "I am a sports person", "I often travel"]
    user_entertainments = []
    if weights[user_name][4] != 0:
        for entertainment in entertainments:
            puntuation = input(f"{entertainment}: ")
            puntuation = enter(puntuation)
            while puntuation > 11 or puntuation < 1:
                puntuation = input(f"Rate from 1 to 10. {entertainment}: ")
                puntuation = enter(puntuation)
            user_entertainments.append(puntuation)

        data_base[user_name][4]= weights[user_name][4]*statistics.mean(user_entertainments)/10

    else:
        data_base[user_name][4]=0
    
    print("\n")

    print(data_base)
    return data_base



def matches(user_name,data_base):
    def numpy_euclidian_distance(point_1, point_2):
            array_1, array_2 = np.array(point_1), np.array(point_2)
            squared_distance = np.sum(np.square(array_1 - array_2))
            distance = np.sqrt(squared_distance)
            return distance     

    df = pd.DataFrame(data_base)
    print(df)
    hasht={}

    for i in range(0,len(df.columns)):
        if df.columns.values[i] != user_name:
            distance = numpy_euclidian_distance(df.loc[:,user_name],df.iloc[:,i])
            value=100-distance*10
            hasht[df.columns.values[i]]=value
    dic=dict(sorted(hasht.items(),key=lambda x:x[1],reverse=True))
    for d in dic:
        print(f"Affinity with {d}: {dic[d]:.0f}%")
    return 
