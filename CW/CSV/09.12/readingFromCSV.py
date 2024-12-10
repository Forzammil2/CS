import csv
'''
#Show whole Record
file = open("patients.csv","r")
records = csv.reader(file)

next(records)  #skip the header row
for r in records:
    print(r)
    
file.close()


#Show specific part only - in this case Name
file = open("patients.csv","r")
records = csv.reader(file)

next(records)  #skip the header row
for r in records:
    print("Firstname:", r[0])
    
file.close()


#Format the information
file = open("patients.csv","r")
records = csv.reader(file)

print("First Name\t Last Name\t Phone Number\t Date of Birth\t Age")
print("----------------------------------------------------------------------")

next(records)  #skip the header row
for r in records:
    print(r[0],"\t\t",r[1],"\t\t",r[2],"\t",r[3],"\t",r[4])
    
file.close()
'''
