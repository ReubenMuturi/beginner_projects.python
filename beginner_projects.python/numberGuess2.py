print("Your loosing score is -2 ")
k = 40
b = 4
c = 77
d = 83
e = 12
while True:
    num = 0
    a = input("Guess a number? ")
    for number in a:
        if int(a) == k or b or c or d or e:
            num += 1
            print("score=", num)
            if num == 5:
                print("You Win!!!")
        if int(a) != k or b or c or d or e:
            num -= 1
            print("score=", num)
            if num == - 2:
                print("You Loose!!!")
                break
