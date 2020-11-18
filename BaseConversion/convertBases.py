def main(userInput):
    if(userInput.nb == 10):
        print('found 10')
        baseTen(userInput)


def baseTen(userInput):
    if(userInput.cn == 2):
        print('found 2')
        baseTentoTwo(userInput)


def baseTentoTwo(userInput):
    factor = 1
    result = int(0)
    while userInput.ni != 0:
        result += (userInput.ni % 2)*factor
        userInput.ni = int(userInput.ni/2)
        factor *= 10
    print(result)
