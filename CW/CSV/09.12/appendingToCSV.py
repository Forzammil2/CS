import csv
record1 = ["Joan","Byrne","0981 45877","2/2/75","45"]
record2 = ["Gideon","Jones","0938 376800","4/7/59","61"]
record3 = ["Ryan", "Maxwell", "0956 62845", "5/7/65", "34"]
record4 = ["Sophia", "Johnson", "0843 12389", "12/11/72", "51"]
record5 = ["Liam", "Anderson", "0912 54678", "3/25/89", "35"]

file = open("patients.csv","a",newline = "")
db = csv.writer(file)
db.writerow(record1)
db.writerow(record2)

#Asking user to input record
fn = input("Enter firstname: ")
ln = input("Enter lastname: ")
ph = input("Enter phone number: ")
dob = input("Enter date of birth in format dd/mm/yy")
age = input("Enter age: ")
db.writerow([fn,ln,ph,dob,age])  #note the square brackets



file.close()