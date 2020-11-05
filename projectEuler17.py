Number0_9 = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
Number10_19 = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
Number20_90_10 = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
Number100_900 = {1:'OneHundred',2:'twohundred',3:'threehundred',4:'fourhundred',5:'fivehundred',6:'sixhundred',7:'sevenhundred',8:'eighthundred',9:'ninehundred'}


def countLetterInNumber(number):
    if number == 1000:
        return len('onethousand')
    if number <10:
        return len(Number0_9[number])
    if number <20:
        return len(Number10_19[number])
    if number <100:
        if number %10 == 0:
            return len(Number20_90_10[number//10])
        else:
            return len(Number20_90_10[number//10]) + len(Number0_9[number%10])
    if number %100 ==0:
        return len(Number100_900[number//100])
    secondpartofnumber = number%100
    secondpartofnumber = countLetterInNumber(secondpartofnumber)
    return secondpartofnumber + len(Number100_900[number//100]) + 3

count = 0
for i in range(1,1001):
    count += countLetterInNumber(i)
print(count)
