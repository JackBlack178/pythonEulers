
number = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

with open('projectEuler18.txt', 'r') as txtFile:
    number2 = txtFile.read()
    txtFile.close()




#Привести к типу данных int и преобразовать все числа по массивам треугольника
def processArray(number):
  number = number.strip().split('\n')
  for i in range(0,len(number)):
	   number[i] = number[i].strip().split(' ')
	   number[i] = [int(x) for x in number[i]]
  return number


#Считаем максимальную сумму снизу
def findMaxSum(number):
  for i in range(len(number)-2,-1,-1):
	    for j in range(len(number[i])):
		      number[i][j] = number[i][j] + max(number[i+1][j], number[i+1][j+1])
  return number[0][0]

print(findMaxSum(processArray(number)))
print(findMaxSum(processArray(number2)))
