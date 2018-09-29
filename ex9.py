
while True:
    number_count = 0

    n = input("Input the password: ")
    for i in list(n):
        if i.isdigit():
            number_count += 1
    if number_count > 0:
        if len(list(n)) >= 8:
            t = len(list(n))
            upper_count = 0
            lower_count = 0
            for i in list(n):
                if i.isupper():
                    upper_count += 1
                if i.islower():
                    lower_count += 1
            if upper_count > 0 and lower_count > 0:
                break
