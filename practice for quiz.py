def finding_biggest_of_two_numbers():
    A = int(input('Enter a number'))
    B = int(input('Enter another number'))
    if(A > B):
        print(A)
    else:
        print(B)

finding_biggest_of_two_numbers()   

def finding_square_and_cube():
    N = int(input('Giev me a number'))
    S = N * N
    C = S * N
    print(S,C)

finding_square_and_cube()

def finding_average_of_any_three_numbers():
    print('Give me three numbers')
    X = int(input())
    Y = int(input())
    Z = int(input())
    S = X + Y + Z
    A = S / 3
    print(A)

finding_average_of_any_three_numbers()