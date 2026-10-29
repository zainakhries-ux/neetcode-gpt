class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for _ in range(iterations):
            df = 2 * x  # Derivative: f'(x) = 2x
            x -= learning_rate * df  # Update rule: x = x -  learning_rate * f'(x)
        return round(x, 5)  # Round final answer to 5 decimal places