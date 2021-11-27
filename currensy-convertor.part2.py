# App where:
# IN money amout
# IN currency
# OUT money amount

input_corrency = input("Choose currency EUR/USD/MDL :") # "USD"
input_amout    = float (input("Enter amout :")) 

rate_USD_to_EUR = 0.8
rate_EUR_to_USD = 1.25
rate_USD_to_MDL = 1
rate_MDL_to_USD = 1.50
rate_EUR_to_MDL = 2
rate_MDL_to_EUR = 4.5

if input_corrency == "USD" :
    moneyEUR = input_amout / rate_EUR_to_USD
    print("You've got: ", moneyEUR, "EUR")
elif  input_corrency == "MDL":
          moneyUSD = input_amout / rate_USD_to_MDL
          print("You've got: ", moneyUSD, "USD")
elif input_corrency == "EUR":
          moneyEUR = input_amout / rate_MDL_to_EUR
          print("You've got: ", moneyEUR, "MDL")
          
else:
    moneyUSD = input_amout / rate_USD_to_EUR
    print("You've got: ", moneyUSD, "USD")

    moneyMDL = input_amout / rate_USD_to_MDL
    print("You've got: ", moneyMDL, "MDL")

    moneyEUR = input_amout / rate_USD_to_MDL
    print("You've got: ", moneyEUR, "EUR")



