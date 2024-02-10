import random

# loop = 10
# for xx in range(loop + 1):
#     print(xx)

# for i in range(15,21):
#     print(i)

# for k in range(20):
#       print(k)
#       if k == 5:
#           break
# else:
#     print("end")

# print("Random numbers")
# for i in range(6):
#     random_number = random.randint(0,100)
#     if random_number % 2 == 0:
#         print("\x1b[1;32m",random_number ,"\x1b[0;30m")
#     else:
#         print("\x1b[1;35m",random_number ,"\x1b[0;30m")

# n = int(input("number: "))
# x = n + 1
# y = x * 2 + 10
# z = y * n
# n = z + y
#
# range_start = input("start: ")
# range_end = int(input("end: "))

#tabl x
for i in range(1,10):
    print('\n')
    for k in range(1, 10):
        print(f"{i}*{k}={i * k}", end=" ")