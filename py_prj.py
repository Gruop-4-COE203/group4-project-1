#EXCHANGE RATE CALCULATOR

print("Welcome to the exchange rate calculation system!\n")

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

print(f"{len(exchange_rates)} types of exchange you can exchange:")
for line in exchange_rates:
    currency, rate = line.split("=")
    print(f"{currency} : {rate}")

while True:
   user_input_convert_from = input("Enter the currency unit you want to convert FROM(e.g. USD, TRY, EUR):").strip().upper()
   user_input_convert_to = input("Enter the currency unit you want to convert TO(e.g. USD, TRY, EUR):").STRİP().UPPER()

   if user_input_convert_from in rates_dict and user_input_covert_to in rates_dict :
      convert_from = user_input_convert_from 
      convert_to = user_input_convert_to
      break
   else:
      print("Invalid currency. Please enter currencies that are listed above.Try again.\n")


#ece 1
          


# Getting user inputs for conversion
#user_input_convert_from = input("\nEnter the currency unit that you want from convert(e.g. USD, TRY, EUR, JPY, SAR, GBP):")

#print(f"{len(exchange_rates)} types of exchange you can exchange:\n")
#for line in exchange_rates:
 #   currency, rate = line.split("=")
  #  print(f"{currency} : {rate}")


# Getting user inputs for conversion
user_input_convert_from = input("Enter the currency unit that you want from convert(e.g. USD, TRY, EUR, JPY, SAR, GBP):")
user_input_convert_to = input("Enter the currency unit that you want to convert from (e.g. USD, TRY, EUR, JPY, SAR, GBP):")


# Converting user inputs to uppercase to match dictionary keys
convert_to = user_input_convert_to.upper()
convert_from = user_input_convert_from.upper()


# Validating user input currency and getting amount to convert
if convert_from in ["USD", "TRY", "EUR", "JPY", "SAR", "GBP"] and convert_to in ["USD", "TRY", "EUR", "JPY", "SAR", "GBP"]:

    #user_input_amount = float(input("Enter the amount of money you want to convert:"))
    user_input_amounts = input("Enter one or more amounts separated by commas (e.g. 100, 250, 500): ").split(",")
    amounts = [float(x.strip()) for x in user_input_amounts]

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
        return f"{amount} {from_currency} equals to: {converted_amount:.2f} {to_currency}"
    else:
        return "Currency not found in exchange_rate.txt file!"
# Calculate using user input

#result = calculate_exchange(convert_from, convert_to, user_input_amount)
#print(result)

#zehra

for amount in amounts:
    result = calculate_exchange(convert_from, convert_to, amount)
    print(result)
#ipek

with open("coversion_log.txt", "a") as log_file:
   log_file.write(f"\n---New Conversion---\n")
   log_file.write(f"From: {convert_from} → To: {convert_to}\n")
   log_file.write(f"Amounts entered: {','.join(map(str, amounts))}\n")
   log_file.write("Results:\n")
   for amount in amounts:
      converted = calculate_exchange(convert_from, convert_to, amount)
      log_file.write(f""{amount} {convert_from} = {converted:.2f} {convert_to}")
   log_file.write("------------------------\n")

print("Your conversion results were also saved in 'conversion_log.txt'" )


#ece 2 

