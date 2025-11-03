#EXCHANGE RATE CALCULATOR
import datetime
import os

def main():
   print("-------- Welcome to the exchange rate calculation system! --------")
   if not os.path.exists("exchange_rate.txt"):
      print("Error:'exchange_rate.txt' file not found! (Be sure it is in the same folder as this program)")
      return
   
   with open("exchange_rate.txt" , "r") as file:
      exchange_rates = [line.strip() for line in file.readlines()]

   rates_dict = {}   
   for line in exchange_rates:
       currency, name_of_money, rate = line.split(";")
       rates_dict[currency] = float(rate)

   print(f"{len(exchange_rates)} types of exchange you can exchange:")
   for line in exchange_rates:
       currency, name_of_money, rate = line.split(";")
       print(f"{currency} , {name_of_money} : {rate}")
   print("\nNote: All exchange rates are based on TRY = 1.0\n")

   while True:
      user_input_convert_from = input("Enter the currency unit you want to convert FROM(Please choose in the list):").strip().upper()
      if user_input_convert_from in rates_dict:
          user_input_amounts = input("Enter one or more amounts separated by commas (e.g. 100, 250, 500): ").split(",")
          amounts = [float(x.strip()) for x in user_input_amounts]
          break
      else:
          print("Invalid currency. Please enter currencies that are listed above.Try again.\n")     
 
   user_input_convert_to = input("Enter the currency unit you want to convert TO(Please choose in the list):").strip().upper()
   if user_input_convert_to not in rates_dict:
       print("Invalid currency. Please enter currencies that are listed above.Try again.\n")

   convert_from = user_input_convert_from
   convert_to = user_input_convert_to

   def get_rate_from_file(currency):
       if currency in rates_dict:
           return rates_dict[currency]
       else:
           return None

   def calculate_exchange(from_currency, to_currency, amount):
       """Calculate conversions for all supported currencies."""
       rate_from = get_rate_from_file(from_currency)
       rate_to = get_rate_from_file(to_currency)   
       if rate_from and rate_to:
           return amount * (rate_from / rate_to)
       else:
           return "Currency not found in exchange_rate.txt file!"
   
   for amount in amounts:
       converted= calculate_exchange(convert_from, convert_to, amount)
       print(f"{amount} {convert_from} equals to: {converted:.2f} {convert_to}")
      
   with open("conversion_log.txt", "a") as log_file:
      log_file.write(f"\n---New Conversion---\n")
      log_file.write(f"Date & Time Information: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
      log_file.write(f"From: {convert_from} → To: {convert_to}\n")
      log_file.write(f"Amounts entered: {','.join(map(str, amounts))}\n")
      log_file.write("Results:\n")
      for amount in amounts:
         converted = calculate_exchange(convert_from, convert_to, amount)
         log_file.write(f"{converted:.2f} {convert_to} \n")
      log_file.write("------------------------\n")
   print("Your conversion results were saved in 'conversion_log.txt'" )

if __name__=="__main__":
    main()
    