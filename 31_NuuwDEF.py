# def greet(*people):
#     print(people)
# greet("Paul", "Atta", "Bimi", "Desmond")
    ##Default keyword argument because it has a default value
# def solve (x=2,y=3,z=4):
    ## Original Wek
# def solve (x,y,z):
#     solution = x * y - z
# print(solution)
    ## Keyword arguments 
# solve(z = 2, y = 4, x = 3)
# solve(y = 4, x = 3, z = 2)
    ##Positional Arguments
#solve(2,5,4)
    ## Dunno
# def you(**Bleh):
#     print(Bleh)

# you(name = 'atta', age = '20', state = 'lagos')

    ## Recurssion 1
# def recurse():
#     print("I am recursing.. YAAYYY!!")
#     recurse()
# recurse()

    ## Recurssion 2 and Default keyword argument
# def recurse(debt = 10):
#     if debt > 1:
#         return
#     print("I am recursing. Inward")
#     recurse(debt-1)
#     print("AND NOW...Outward!! >.<")
# recurse()

    ## Factorial Tests
    ## It's recursing, like a loop until n finally == 1
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# n_fact = factorial(5)
# print(n_fact)

# def factorial(a, b, d, e, f, g, h):
# Cash = [20, 70, 100, 120, 160, 165, 171]
# for x in range (len(Cash)):
#     if x == len(Cash) -1:
#         break
#     Savings = Cash[x+1] - Cash[x]

# # n_fact = factorial(5)
#     print(Savings)

def roam(balance):
    if len(balance)<2:
        return
    else:
        print(balance[1]-balance.pop(0)
        return roam(balance)
        