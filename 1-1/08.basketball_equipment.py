year_tax = int(input())
 
shoes_price = year_tax - (year_tax * 0.40)
suit_price = shoes_price - (shoes_price * 0.20)
ball_price = suit_price / 4
acc_price = ball_price / 5
 
total_price = year_tax + shoes_price + suit_price + ball_price + acc_price
 
print(total_price)