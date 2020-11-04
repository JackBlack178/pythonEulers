lenghtOfNumbers = 0


for i in range(1000000,1,-1):
        listOfNumbers = []
        number = i
        while number != 1 :
            if number%2 == 0:
                number /= 2
                listOfNumbers.append(number)
            else:
                number = number*3 + 1
                listOfNumbers.append(number)
        if len(listOfNumbers) > lenghtOfNumbers:
            lenghtOfNumbers = len(listOfNumbers)
            findNumber = i
print(findNumber)
