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

# check "TRY" in the rates file , if is not adding it manually
if "TRY" not in rates_dict:
    rates_dict["TRY"] = 1.0

# How many exchange rates loaded
print(f"{len(exchange_rates)} types of exchange you can exchange:\n")
for line in exchange_rates:
    currency, rate = line.split("=")
    print(f"{currency} : {rate}")


# Getting user inputs for exchange with indexes 
user_input_convert_from = input("Enter the currency unit that you want from convert(e.g. USD, TRY, EUR, JPY, SAR, GBP):")
user_input_convert_to = input("Enter the currency unit that you want to convert from (e.g. USD, TRY, EUR, JPY, SAR, GBP):")


# Converting user inputs to uppercase to match dictionary keys
convert_to = user_input_convert_to.upper()
convert_from = user_input_convert_from.upper()


# Validating user input currency and getting amount to convert
if convert_from in ["USD", "TRY", "EUR", "JPY", "SAR", "GBP"] and convert_to in ["USD", "TRY", "EUR", "JPY", "SAR", "GBP"]:
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
    
# Function to calculate exchange between two currencies,
def calculate_exchange(from_currency, to_currency, amount):
    """Calculate conversions for all supported currencies."""
    rate_from = get_rate_from_file(from_currency)
    rate_to = get_rate_from_file(to_currency)   
    if rate_from and rate_to:
        converted_amount = amount * (rate_from / rate_to)
        return f"{amount} {from_currency} equals to: {converted_amount} {to_currency}"
    else:
        return "Currency not found in exchange_rate.txt file!"
# Calculate using user input
result = calculate_exchange(convert_from, convert_to, user_input2)
print(result)

