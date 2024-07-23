#Cambio de divisas

def exchange_money(budget, exchange_rate):
    result = budget/exchange_rate
    return result

def get_change(budget, exchanging_value):
    result = budget - exchanging_value
    return result
   
def get_value_of_bills(denomination, number_of_bills):
    result = denomination * number_of_bills
    return result

def get_number_of_bills(budget, denomination):
    result = int(budget/denomination)
    return result
  
def get_leftover_of_bills(budget, denomination):
    result = budget % denomination
    return result

def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_decimal = spread / 100
    adjusted_exchange_rate = exchange_rate * (1 + spread_decimal)
    max_new_currency = budget / adjusted_exchange_rate
    units_in_denomination = max_new_currency // denomination
    exchangeable_amount = units_in_denomination * denomination
    return int(exchangeable_amount)
