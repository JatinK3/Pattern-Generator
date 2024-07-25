for i in range(1,5):
    for j in range(i):
        print('*',end=" ")
    print()

n=5
for i in range(5):
    for j in range(n-i):
        print('*',end=" ")
    print()

n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=" ")
#     for j in range(i+1):
#         print('*',end=" ")
#     for j in range(i):
#         print('*',end=" ")
#     print()

def pyramid_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

pyramid_pattern(5)
