company_name = input()

adult_tickets_count = int(input())
kid_tickets_count = int(input())

adult_tickets_price = float(input())
service_price = float(input())

kid_tickets_price = adult_tickets_price - (adult_tickets_price * 0.7)

adult_tickets_price += service_price
kid_tickets_price += service_price

all_tickets_price = (kid_tickets_count * kid_tickets_price) + (adult_tickets_count * adult_tickets_price)

profit = all_tickets_price * 0.2

print(f'The profit of your agency from {company_name} tickets is {profit:.2f}')
