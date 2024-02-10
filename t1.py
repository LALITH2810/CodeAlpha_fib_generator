def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    print(f"The Fibonacci series up to the {n}th number is:", end=" ")
    print_fibonacci_series(n)
