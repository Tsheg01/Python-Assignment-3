def calculate_discount(price, discount_percent):
    # Apply discount only if it's 20% or more
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)

    # Print the result
    print(f"Final price: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")

