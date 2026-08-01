def divide_numbers(a: float, b: float) -> float:
    # Potential ZeroDivisionError if b == 0
    return a / b

def calculate_discount(price: float, discount_percent: float) -> float:
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount percentage")
    return price * (1 - discount_percent / 100)
