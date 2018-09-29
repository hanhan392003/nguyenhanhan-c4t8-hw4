while True:
    n = input("Please enter your name : ")
    if n.isalpha():
        break
    else:
        print("Your name can't have numbers or special characters")
