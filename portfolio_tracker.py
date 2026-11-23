```python
import csv

def track_portfolio():
    # Hardcoded stock prices (in USD)
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 140.50,
        "MSFT": 370.00,
        "AMZN": 145.00
    }

    portfolio = []
    total_investment = 0.0

    print("=== Stock Portfolio Tracker ===")
    print("Available Stocks & Current Prices:")
    for ticker, price in stock_prices.items():
        print(f"  {ticker}: ${price:.2f}")
    print("\nEnter stock details (type 'done' when finished):")

    while True:
        ticker = input("\nEnter Stock Ticker (e.g., AAPL): ").upper().strip()
        if ticker == "DONE":
            break
        
        if ticker not in stock_prices:
            print("Stock not found in database. Please choose from the available list.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {ticker}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer for quantity.")
            continue

        price = stock_prices[ticker]
        value = price * quantity
        total_investment += value

        portfolio.append({
            "Ticker": ticker,
            "Quantity": quantity,
            "Price": price,
            "Total_Value": value
        })
        print(f"Added {quantity} shares of {ticker} (${value:.2f})")

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    # Display summary
    print("\n--- Portfolio Summary ---")
    for item in portfolio:
        print(f"{item['Ticker']} | Qty: {item['Quantity']} | Price: ${item['Price']:.2f} | Subtotal: ${item['Total_Value']:.2f}")
    print(f"Total Investment Value: ${total_investment:.2f}")

    # Optional CSV Export
    save_choice = input("\nWould you like to save this report to a CSV file? (y/n): ").lower().strip()
    if save_choice == 'y':
        filename = "portfolio_summary.csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Ticker", "Quantity", "Price", "Total_Value"])
            writer.writeheader()
            writer.writerows(portfolio)
            writer.writerow({"Ticker": "TOTAL", "Quantity": "", "Price": "", "Total_Value": total_investment})
        print(f"Report saved successfully to {filename}!")

if __name__ == "__main__":
    track_portfolio()
