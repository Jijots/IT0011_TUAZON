month = input("Enter the month (numerical): ")
day = input("Enter the day (numerical): ")
year = input("Enter the year (numerical): ")

monthword = ""
if month == "1":
    monthword = "January"
elif month == "2":
    monthword = "February"
elif month == "3":
    monthword = "March"
elif month == "4":
    monthword = "April"
elif month == "5":
    monthword = "May"
elif month == "6":
    monthword = "June"
elif month == "7":
    monthword = "July"
elif month == "8":
    monthword = "August"
elif month == "9":
    monthword = "September"
elif month == "10":
    monthword = "October"
elif month == "11":
    monthword = "November"
elif month == "12":
    monthword = "December"
else:
    monthword = "Invalid month"

print("Original Date: " + month + "/" + day + "/" + year)
print("The date is: ", monthword, day + ",", year)