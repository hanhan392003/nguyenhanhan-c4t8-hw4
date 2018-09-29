print (''' How many legs does a spider have ?
    1. None
    2. 4 legs
    3. 8 legs
    4. 12 legs''')
time = 1
while True:
    try :
        
        answer = int(input("Your answer : "))
        if answer == 3:
            break
        elif answer > 0 and answer <= 4 :
            time += 1
            if time > 5 :
                print("Wrong, the answer is 3 : 4 legs")
                break
        else:
            print("The answer must be 1, 2, 3 or 4, please enter again")

    except ValueError:
        print("The answer must be 1, 2, 3 or 4, please enter again")



    
