# by vincent
# date 2024-10-10
# goal to make a random number guesser

import random



gametype = str(input("Input Difficulty easy, hard, impossible: ")).lower()

    


count = 1

run = True


if gametype == "easy":
    num = random.randint(1,100)
    
            
    while run:

        try:
            
            guess=int(input("guess "))
            if guess == (num):
                print("good job")
                print(f"it took you {count} attemps to guess")
                run=False
                
            elif guess >= (num+50):
                print("freezing too high")
                count=count+1
                
            elif guess <= (num-50):
                print("freezing too low")
                count=count+1
                
            elif guess >= (num+25):
                print("cold too high")
                count=count+1
            
            elif guess <= (num-25):
                print("cold too low")
                count=count+1
                
            elif guess >= (num+15): 
                print("cool too high")
                count=count+1
            
            elif guess <= (num-15):
                print("cool too low")
                count=count+1
                
            elif guess >= (num+10): 
                print("warm too high")
                count=count+1
            
            elif guess <= (num-10):
                print("warm too low")
                count=count+1
            
            elif guess >= (num+5): 
                print("hot too high")
                count=count+1
            
            elif guess <= (num-5):
                print("hot too low")
                count=count+1
                
            elif (guess <= (num+4)) or (guess >= (num-4)):
                print("boiling within 5")
                count=count+1
                
        except: print("whole numbers only")


elif gametype == "hard":
    num =random.randint(1,100)
    
    
    run2=True
    while run2 == True:
        try:
            guess=int(input("guess "))
            if guess > num:
                print ("lower")
                count=count+1
                
            elif guess < num:
                print ("higher")
                count=count+1
                
            if guess == num:
                print ("you win good job")
                run2 = False
                print(count)
        except:
            print("numbers only")
    

elif gametype == "impossible":
    run3=True
    while run3==True:
        try:
            num =random.randint(1,100)
            print (num)
            guess=int(input("guess "))
            count=count+1
            if guess == num:
                print("lucky bastard")
                print(count)
                run3 = False
            else:
                print(f"the number was {num}")
                pass
        except:
            print("numbers only")