def fibonacci(n): #define a function
    if n <= 1:  #to check the n whether it is below the one or not, since fibonaccis starts from 1
        return n
    fib = [0] * (n + 1) # memory to store the fibonacci results
    fib[1] = 1 #initial values

    for i in range(2, n + 1):   # calculate the fibonacci using tabulation approach
        fib[i] = fib[i - 1] + fib[i - 2] #stores the valued in the memory

    return fib[n]

# test the function
n = 8
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is {result}")
