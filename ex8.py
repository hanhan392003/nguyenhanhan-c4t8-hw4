while True:
    number_count = 0
    n = input("Please enter password ")
    for i in list(n):
        if i.isdigit():
            number_count += 1
    if number_count > 0:
        if len(list(n)) >= 8:
            break