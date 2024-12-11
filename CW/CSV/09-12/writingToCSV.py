import csv
header = ["firstname","lastname","phonenum","dob","age"]
file = open("patients.csv","w",newline="")
db = csv.writer(file)
db.writerow(header)
file.close()