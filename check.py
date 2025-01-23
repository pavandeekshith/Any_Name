def fibonacci(n):
    """Generate Fibonacci sequence up to the nth number."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    """Main function."""
    try:
        n = int(input("Enter the number of Fibonacci terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        fib_sequence = fibonacci(n)
        print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")

        primes_in_fib = [num for num in fib_sequence if is_prime(num)]
        print(f"Prime numbers in the Fibonacci sequence: {primes_in_fib}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
