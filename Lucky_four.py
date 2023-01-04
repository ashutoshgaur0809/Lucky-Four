T = int(input("Enter how many test cases you want = "))
for i in range(T):
    n = int(input("Enter an no- "))
    l = len(str(n))
    count = 0
    for i in range(l):
        a = n % 10
        if (a % 4 == 0):
            count = count+1
        n = n // 10
    print("ocuurence of  4 is", count)
