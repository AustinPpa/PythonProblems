marked_price = int(input('Enter marked price: '))
gender = input('Enter gender: ')

if gender == 'M':
    if marked_price < 10000:
        print(f'Discount: No discount \nNet Amount: {marked_price}')
    elif 10000 <= marked_price < 20000:
        discount = 0.10 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')
    elif 20000 <= marked_price < 50000:
        discount = 0.15 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')
    elif marked_price >= 50000:
        discount = 0.20 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')

elif gender == 'F':
    if marked_price < 10000:
        discount = 0.05 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')
    elif 10000 <= marked_price < 20000:
        discount = 0.15 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')
    elif 20000 <= marked_price < 50000:
        discount = 0.20 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')
    elif marked_price >= 50000:
        discount = 0.25 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')

elif gender == 'L' or gender == 'G' or gender == 'B' or gender == 'T':
    if marked_price < 10000:
        discount = 0.10 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')
    elif 10000 <= marked_price < 20000:
        discount = 0.20 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')
    elif 20000 <= marked_price < 50000:
        discount = 0.25 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')
    elif marked_price >= 50000:
        discount = 0.30 * marked_price
        net_amount = marked_price - discount
        print(f'Discount: {discount} \nNet Amount: {net_amount}')

else:
    print(f'Discount: Try Again \nNet Amount: Try again')