# Create a list (dictionary) of months and their standard number of days.
month_days = {
    1:31, # January
    2:28, # Febuary
    3:31, # March
    4:30, # April
    5:31, # May
    6:30, # June
    7:31, # July
    8:31, # August
    9:30, # September
    10:31, # October
    11:30, # November
    12:31 # December
}
month_number = int(input ("Enter the month (1-12):"))
# Check if the number is valid (1-12).
if month_number in month_days:
    # If the month is February (2):
    if month_number == 2:
       # Ask if it is a leap year.
        Leap_year = input("Is it a leap year? (yes/no):").lower()
       # If YES, print 29 days. 
        if Leap_year == "yes":
            print(f"month 2 (February) has 29 days because its a leap year.")
       # If NO, print 28 days.
        else:
            days = month_days [month_number]
            print(f"month 2 (february) has {days} days.")
    # If it is any other month: 
    else:
        # Print the standard number of days for that month.
        days = month_days[month_number]
        print(f"month {month_number} has {days} days.")
# If the number is NOT valid (e.g., 13):
else:
    # Print an error message.
    print("woah: gotta be only 1-12 buddy")