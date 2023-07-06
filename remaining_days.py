weeks = int(input("Enter a project timeframe in weeks: "))
past_days = int(input("Enter past working days: "))

weeks_in_days = weeks * 7
remaining_days = weeks_in_days - past_days

myStr = f"The remaining days before the deadline are {remaining_days} days."
length = len(myStr)
print("*" * (2+length))
print(f"*{myStr}*")
print("*" * (2+length))


