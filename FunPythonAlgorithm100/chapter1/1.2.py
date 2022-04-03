if __name__=="__main__":
    n = int(input())
    fib1 = 1
    fib2 = 1
    i = 3
    print("%6d       %6d" %(fib1, fib2), end="       ")
    while i <= n:
        fib = fib1 + fib2 
        print("%6d" %fib, end="       ")   
        if i % 4 == 0:
            print()   
        fib2 = fib1  
        fib1 = fib   
        i += 1
