def fibonacci(n):
    """
    Generate a list containing the first n Fibonacci numbers.
    
    Parameters:
    n (int): The number of Fibonacci numbers to generate.
    
    Returns:
    list: A list containing the first n Fibonacci numbers.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input n must be an integer.")
    if n <= 0:
        raise ValueError("Input n must be a positive integer.")
        
    # Generate Fibonacci sequence
    sequence = []
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)
        
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
        
    return sequence
# Test the Fibonacci function with valid inputs
for val in [1, 2, 5, 10]:
    print(f"First {val} Fibonacci numbers: {fibonacci(val)}")

# Test input validation
try:
    fibonacci(0)
except ValueError as e:
    print(f"Validation check passed for non-positive input: {e}")

try:
    fibonacci("5")
except TypeError as e:
    print(f"Validation check passed for non-integer input: {e}")
