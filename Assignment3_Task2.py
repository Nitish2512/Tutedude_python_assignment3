while True:
    num = input("Enter a number:")
    if not num.isdigit():
        print ("Enter a valid number")
        continue

    num = float(num)
    print ("Square root:", math.sqrt(num))
    print ("Logarithm:", math.log(num))
    print ("Sine:", math.sin(num))
    break