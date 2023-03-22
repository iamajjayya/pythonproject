import random
def hangman():

    listOfwords = ["kannada","telugu","tamil","malyalam","hindi"]
    word =random.choice(listOfwords)
    turns = 10
    guessmade = ''
    validateentries= set('abcdefghijklmnopqrstuvwxyz')


    while len(word)>0:
            main_word = ""
        

            for letter in word:
                if letter in guessmade:
                    main_word = main_word+letter
                else:
                    main_word = main_word+"_ "    
            if main_word == word:
                print(main_word)
                print(" You won!!! 🎉🎊🎉🍾")
                break
                    
        
            print(" guess the word",main_word)
            guess = input()

            if guess in validateentries:
                guessmade=guessmade+guess
            else:
                print("enter valid character")
                guess =input()  
            if guess not in word:
                turns = turns-1

                if turns==9:
                    print("9 turns left!")
                    print("-------------------")  
                if  turns==8:
                    print("8 turns left!")
                    print("-------------------")    
                    print("        O          ")    
                if  turns==7:
                    print("7 turns left!")
                    print("-------------------")    
                    print("        O          ") 
                    print("        |           ") 
                if  turns==6:
                    print("6 turns left!")
                    print("-------------------")    
                    print("        O          ") 
                    print("        |          ")  
                    print("       /           ") 

                if  turns==5:
                    print("5 turns left!")
                    print("-------------------")    
                    print("        O          ") 
                    print("        |          ")  
                    print("       / \         ") 
                if  turns==4:
                    print("4 turns left!")
                    print("-------------------")    
                    print("      \ O          ") 
                    print("        |          ")  
                    print("       / \         ") 
                                    
                if  turns==3:
                    print("3 turns left!")
                    print("-------------------")    
                    print("      \ O /         ") 
                    print("        |          ")  
                    print("       / \         ") 
                if  turns==2:
                    print("2 turns left!")
                    print("-------------------")    
                    print("      \ O /   |      ") 
                    print("        |          ")  
                    print("       / \         ")     
                if  turns==1:
                    print("1 turns left! hangman on his last breath")
                    print("-------------------")    
                    print("      \ O /_|       ") 
                    print("        |          ")  
                    print("       / \         ") 
                if  turns==0:
                    print("You Lose")
                    print(" Word is",word)    
name = input("Enter your Name ")
print("Welcome " , name , "!")
print("---------------------")
print("Try to guess the word in less then 10 attempts ")
hangman()
