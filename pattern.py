import math
hollow_shapes=['hollow_square','hollow_triangle','hollow_diamond']
shapes = ['square', 'triangle', 'diamond','pyramid','circle']
shapes.extend(hollow_shapes)
def get_user_input():
    shape = input(f"Enter Shape of Your Choice from {shapes}: ").strip().lower()
    n = int(input("Enter the Size of Pattern(n): "))
    return n, shape


def square_pattern(n):
    for i in range(n):
        print("* " * n)

def triangle_pattern(n):
   for i in range(n):
        for j in range(n-i-1):
            print(' ',end=" ")
        for j in range(i+1):
            print('*',end=" ")
        for j in range(i):
            print('*',end=" ")
        print()

def pyramid_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

def diamond_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for i in range(n - 1):
        print(' ' * (i + 1) + '* ' * (n - i - 1))

def display_pattern(n, shape):
    function_name = shape + '_pattern'
    if shape in shapes:
        try:
            function = globals()[function_name]
            function(n)
        except KeyError:
            print(f"No function found for shape: {shape}")
    else:
        print("Enter valid Shape")

def hollow_square_pattern(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print('* ' * n)
        else:
            print('* ' + '  ' * (n-2) + '*')

def hollow_triangle_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1), end=' ')
        
        if i == 0 or i == n - 1:
            print('* ' * (i + 1))
        else:
            print('* ' + '  ' * (i - 1) + '*')

    
def hollow_diamond_pattern(n):
    for i in range(n):
        if i == 0:
            print(' ' * (n - i - 1) + '*')
        else:
            print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*')
    for i in range(n - 2, -1, -1):
        if i == 0:
            print(' ' * (n - i - 1) + '*')
        else:
            print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*')

def circle_pattern(radius):
    for i in range((2 * radius) + 1):
        for j in range((2 * radius) + 1):
            dist = math.sqrt((i - radius) ** 2 + (j - radius) ** 2)
            if dist < radius + 0.5 and dist > radius - 0.5:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


def main():
    n,shape=get_user_input()
    display_pattern(n,shape)

if __name__=="__main__":
    main()