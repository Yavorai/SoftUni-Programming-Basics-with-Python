pen_count = int(input())
markers_count = int(input())
detergent_lt = int(input())
discount_percent = int(input())
 
price_pen = pen_count * 5.80
price_markers = markers_count * 7.2
price_detergent = detergent_lt * 1.20
 
all_price = price_pen + price_markers + price_detergent
discount = all_price * (discount_percent / 100)
total_sum = all_price - discount
 
print(total_sum)