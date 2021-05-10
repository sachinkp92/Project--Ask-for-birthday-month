#Project- Ask for Birthday format DD-MM_YY, You were born in
birthday=input("Enter your birthday in the format DD-MM-YYYY:")
months=("January","Febuary","March","April","May","June","July","August","September","October","November","December")
index=int(birthday[3:5])-1
bd_month=months[index]
print("You were born in",bd_month)
