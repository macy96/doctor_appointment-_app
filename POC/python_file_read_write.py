# # WRITE file
# with open('dog_breeds.txt', 'a') as writer:
#     # Alternatively you could use
#     # writer.writelines(reversed(dog_breeds))

#     # Write the dog breeds to the file in reversed order
#     dog_breeds =["dog-type1", "dog-type2", "dog-type3", "dog-type4"]

    # for breed in dog_breeds:
    #     writer.write(breed + "\n")

# # READ file
# with open('dog_breeds.txt', 'r') as reader:
#     # Note: readlines doesn't trim the line endings
#     dog_breeds = reader.readlines()
#     print(dog_breeds)




import csv

# with open('employee_file.csv', mode='a') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     {"appointment_number":1, "name":"Manas","age":35,"doctor":"optimetrist","doctorname":"Mr Laurent"}


#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


import csv
  
# employee_info = ['appointment_number', 'name', 'age','doctor','doctorname']
  
# new_dict = {"appointment_number":1, "name":"Manas","age":35,"doctor":"optimetrist","doctorname":"Mr Laurent"}

  
# with open('doctor_appointment_database.csv', 'a', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames = employee_info)
#     writer.writeheader()
#     writer.writerow(new_dict)

# with open("E:\doctor-appointment-main\backend\doctor_appointment_database.csv", 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     filecontent = reader.readlines()
#     print("FileContent: {}".format(filecontent))

import csv
with open(r"E:\doctor-appointment-main\backend\doctor_appointment_database.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # print("FileContent: {}".format(reader.readlines()))
    print([row for row in reader])
    #     print(row)
