# Calculate factorial iteratively
def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Parameters:
    n (int): The number to find the factorial of.
    
    Returns:
    int: The factorial of the number.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
        
    # Factorial calculation
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Test the function with valid inputs
for val in [0, 1, 5, 10]:
    print(f"Factorial of {val} is: {factorial(val)}")

# Test input validation
try:
    factorial(-3)
except ValueError as e:
    print(f"Validation check passed for negative input: {e}")

try:
    factorial(5.5)
except TypeError as e:
    print(f"Validation check passed for non-integer input: {e}")
