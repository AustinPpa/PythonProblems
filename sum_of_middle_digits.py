myNum = int(input("Enter a number: "))
tens_digit = myNum // 10
if tens_digit > 100:
    two_digit = tens_digit % 100
    front = two_digit // 10
    end = two_digit % 10
    sum = front + end
else:
    sum = tens_digit % 10





print("*"*sum+f"{sum}"+"*"*sum)
print(145 // 100)