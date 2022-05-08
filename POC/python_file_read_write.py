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

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])