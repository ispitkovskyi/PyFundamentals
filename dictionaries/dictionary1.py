#Declare dictionary
monthConversions =  {
    0: "Zero",
    1: "One",
    10: "Ten",
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

#Accessing elements of dictionary
print(monthConversions["Nov"])
#Alternative way
print(monthConversions.get("Dec"))
#Using invalid key, and passing custom value for invalid key
print(monthConversions.get("Luv", "Not a valid key"))