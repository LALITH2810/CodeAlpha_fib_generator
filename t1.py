def fibonacci(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def print_fibonacci_series(n):
    for i in range(1, n + 1):
        print(fibonacci(i), end=" ")

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
        print(f"The Fibonacci series up to the {n}th number is:", end=" ")
        print_fibonacci_series(n)
