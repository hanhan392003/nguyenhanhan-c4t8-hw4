while True :
    number_count = 0
    n = input("Please input the password : ")
    for i in list(n):
        if i.isdigit():
            number_count += 1
    if number_count > 0 :
        break
    else:
        print("Your password must include at least one number")
