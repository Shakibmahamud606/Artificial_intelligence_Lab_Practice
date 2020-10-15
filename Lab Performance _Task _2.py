sk = int(input())
if sk > 1:
    for i in range(2, sk):
        if (sk % i) == 0:
            print(sk, "is not a prime number")
            break
    else:
        print(sk, "is a prime number")
else:
    print(sk, "is not a prime number")
