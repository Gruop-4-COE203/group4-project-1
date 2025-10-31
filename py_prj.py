#EXCHANGE RATE CALCULATOR

print("Welcome to the exchange rate calculation system!")

# Loading exchange rates from file
with open("exchange_rate.txt" , "r") as file:
   exchange_rates = [line.strip() for line in file.readlines()]

# Converting exchange rates to a dictionary
rates_dict = {}
for line in exchange_rates:
    currency, rate = line.split("=")
    rates_dict[currency] = float(rate)

# Getting user input for currency   
user_input = input("Enter the currency unit that you want to convert(e.g. USD, TRY, EUR, JPY, SAR, GBP):")
currency = user_input.upper()

# Validating user input currency and getting amount to convert
if currency in ["USD", "TRY", "EUR", "JPY", "SAR", "GBP"]:
    print("Your currency is:", currency)
    user_input2 = float(input("Enter the amount of money you want to convert:"))
else:
    print("Invalid currency.Please try again!")
    exit()

# Function to get exchange rate from the loaded dictionary
def get_rate_from_file(currency):
    """Fetch exchange rate dynamically from the loaded dictionary."""
    if currency in rates_dict:
        return rates_dict[currency]
    else:
        return None
    
# Function to calculate exchange
def calculate_exchange(currency, money):
    """Calculate the conversion using the fetched rate."""
    rate = get_rate_from_file(currency)
    if rate:
        return f"{money} {currency} equals to: {money * rate:.2f} TRY"
    else:
        return "Currency not found in exchange_rate.txt file!"

# Calculate using user input
result = calculate_exchange(currency, user_input2)
print(result)
