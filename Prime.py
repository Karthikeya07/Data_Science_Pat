n = int(input("Enter a number "))
if n > 1:
    for i in range(2, int((n)**(1/2))):
        if (n % i) == 0:
            print(n, "is not a Prime")
            break
    else:
        print(n, "is a Prime")
else:
    print(n, "is not a Prime")

eo = "is Even" if n % 2 == 0 else "is Odd"
print(n, eo)

div5 = "is Divisible by 5" if n % 5 == 0 else "is Not Divisible by 5"
print(n, div5)

cnt = 0
for i in range(n+1):
    cnt += i
print("Sum of numbers upto", n, "is:-", cnt)
