age = int(input("What is your current age?\n"))

# there are 365 days in a year
# there are 52 weeks in a year
# there are 12 months in a year

#convert years to days, weeks:
day = age * 365
week = age * 52
month = age * 12

# calculate the remaining days
new_day = (90 * 365) - day
new_week = (90 * 52) - week
new_month = (90 * 12) - month
# the final presentation:
print(f"You have {new_day} days, {new_week} weeks, and {new_month} months left.")
