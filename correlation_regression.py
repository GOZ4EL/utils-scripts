"""
This module is written for educational purpouses, and it
intends to make less tedious the procces of solving correlation
and regression basic problems.
"""
def main():
    """
    Main function, intendet to be the main algorithm, and the
    one function to be executed when the script is runned
    """
    n = float(input('n:\n'))
    value_pairs = get_value_pairs(n)

    x_sum = get_x_sum(value_pairs)
    y_sum = get_y_sum(value_pairs)
    x_per_y_sum = get_x_per_y_sum(value_pairs) 
    x_pow_sum = get_x_pow_sum(value_pairs)

    a0 = compute_a0(y_sum=y_sum, x_pow_sum=x_pow_sum, 
                    x_sum=x_sum, x_per_y_sum=x_per_y_sum, n=n)
    a1 = compute_a1(n=n, x_per_y_sum=x_per_y_sum, x_sum=x_sum,
                    y_sum=y_sum, x_pow_sum=x_pow_sum)

    linear_regression_line = compute_linear_regression_line(a0, a1)

    print(f'x = {x_sum}',
          f'y = {y_sum}',
          f'x per y = {x_per_y_sum}',
          f'x pow 2 = {x_pow_sum}',
          f'a0 = {a0}',
          f'a1 = {a1}',
          f'y = {linear_regression_line}',
          sep='\n')
    

def get_value_pairs(n):
    """
    Get all the (x,y) values pairs of the problem.
    """
    value_pairs = []
    for i in range(int(n)):
        x = float(input(f'x #{i}:'))
        y = float(input(f'y #{i}'))
        value_pairs.append([x, y])
    return value_pairs 


def get_x_sum(value_pairs):
    """
    Computes and returns the sum of all x values.
    """
    result = 0
    for pair in value_pairs:
        result += pair[0]
    return result


def get_y_sum(value_pairs):
    """
    Computes and returns the sum of all y values.
    """
    result = 0
    for pair in value_pairs:
        result += pair[1]
    return result


def get_x_per_y_sum(value_pairs):
    """
    Computes and returns the sum of all the value pairs multiplied.
    """
    result = 0
    for pair in value_pairs:
        result += pair[0] * pair[1]
    return result


def get_x_pow_sum(value_pairs):
    """
    Computes and returns the sum of all the x raised to power 2.
    """
    result = 0
    for pair in value_pairs:
        result += pair[0]**2
    return result


def compute_a0(y_sum, x_pow_sum, x_sum, x_per_y_sum, n):
    """
    Computes and returns the a0.
    """
    return (
            ((y_sum * x_pow_sum) - (x_sum * x_per_y_sum)) /
            ((n * x_pow_sum) - (x_sum**2)))


def compute_a1(n, x_per_y_sum, x_sum, y_sum, x_pow_sum):
    """
    Computes and returns the a1.
    """
    return (
            (n * x_per_y_sum - x_sum * y_sum) /
            (n * x_pow_sum - x_sum**2))


def compute_linear_regression_line(a0, a1):
    """
    Returns the linear regression line function as a string.
    """
    return f'{a0} + {a1}x'


main()
