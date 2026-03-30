def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations using 
    the gradient of ax^2 + bx + c.
    """
    x = x0
    
    for _ in range(steps):
        # 1. Calculate the gradient (derivative) at the current x
        # f'(x) = 2ax + b
        gradient = 2 * a * x + b
        
        # 2. Update x by moving opposite to the gradient
        # x_new = x_old - learning_rate * gradient
        x = x - lr * gradient
        
    return x