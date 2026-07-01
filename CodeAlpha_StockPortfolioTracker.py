# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# Number of different stocks
n = int(input("How many stocks do you want to enter? "))

portfolio_data = []

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        portfolio_data.append(
            f"{stock}, Quantity: {quantity}, Value: ${investment}"
        )

        print(f"Value of {stock}: ${investment}")
    else:
        print("❌ Stock not found!")

print("\n📊 Portfolio Summary")
for item in portfolio_data:
    print(item)

print(f"\n💰 Total Investment Value: ${total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("----------------------\n")

    for item in portfolio_data:
        file.write(item + "\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\n✅ Portfolio saved to 'portfolio.txt'")
