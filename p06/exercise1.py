import random


#list_1 = [2, 22, 3, 4, 88]



# length = len(list_1)
# print('len = %d' % length)
#
# for i in range(length):
#     print(list_1[i])

# for i in list_1:
#     print(i)

# new_list =[]
#
# for i in range(51):
#     x = random.randint(0,1000)
#     new_list.append(x)
# print(new_list)
# new_list =[]
#
# for i in range(11):
#     new_list.append(random.randint(0,10))
#
# sum = 0
# for i in new_list:
#     if i % 2 == 0:
#         sum += i
#
# print(new_list)
# print('Sum = %d' % sum)

# histogram = []
# for i in range(50):
#     histogram.append(random.randint(0,10))
#
# print(histogram)
#
# for i in histogram:
#     red = ''
#     if i > 5:
#         red = '\x1b[0;31m'
#
#     print(red, '\u2588'*i, i, '\x1b[0;30m')

# numbers =[]
# for i in range(10):
#     numbers.append(random.randint(1,5))
#
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
#
# print(numbers)
# print(unique)

# numbers = [random.randint(0,10) for i in range(10)]
# print(numbers)

# numbers = [i*i for i in range(10)]
# print(numbers)
#
# file = open('num.txt', 'w')
# for n in numbers:
#     file.write("%s\n" % n)
#
# file.close()

numbers_from_file = []
file = open('num.txt', 'r')
for n in file.readlines():
    numbers_from_file.append(int(n))

print(numbers_from_file)