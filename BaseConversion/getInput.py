class numToConvert():
    def __init__(self, numberInput, numberBase, convertNumber):
        self.ni = numberInput
        self.nb = numberBase
        self.cn = convertNumber

def main():
    numberInput = int(input('Please enter an integer: '))
    numberBase = int(input('Please input the starting base(10,8,6,2): '))
    convertNumber = int(input('Please input the base you want converted to(10,8,6,2): '))

    newNumber = numToConvert(numberInput,numberBase,convertNumber)

    return newNumber