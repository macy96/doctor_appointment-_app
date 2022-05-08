from flask import Flask, request, jsonify
import flask
import json
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

# Write the header only once
appointment_table_header = ['appointment_number', 'name', 'age','doctor','doctorname']
with open('doctor_appointment_database.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = appointment_table_header)
    writer.writeheader()

# map as database 
appointments = [
    {"appointment_number":1, "name":"Manas","age":35,"doctor":"optimetrist","doctorname":"Mr Laurent"}
]

# Get all appointments
@app.get("/appointment")
def get_appointments():
    print("get appointments called: {}".format(appointments))

    # Read it from the csv database
    with open(r"E:\doctor-appointment-main\backend\doctor_appointment_database.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # print("FileContent: {}".format(reader.readlines()))
        all_appointments_from_db = [row for row in reader]
        print(all_appointments_from_db)
        return jsonify(all_appointments_from_db)

# Get all appointments
@app.get("/appointment/{appointment_number_param}")
def get_appointment_by_id(appointment_number_param):
    print("get appointments called: {}".format(appointments))

    for appointment in appointments:
        if appointment["appointment_number"] == appointment_number_param:
            return jsonify(appointment)
    return jsonify({"error": "appointment not found"})

# Generate an unique appointment id
def _find_next_id(): 
    print("appointments: {}".format(appointments))
    return max(appointment["appointment_number"] for appointment in appointments) + 1

# Create a new appointment
@app.route('/appointment', methods=["POST"])
def create_appointment():
    if request.is_json:
        new_appointment = request.get_json()
        new_appointment["appointment_number"] = _find_next_id()
        appointments.append(new_appointment)
        print("appointments: {}".format(appointments))
        add_new_appointment_to_database(new_appointment)
        return new_appointment, 201
    return {"error": "Request must be JSON"}, 415

def add_new_appointment_to_database(new_appointment):
    # new_dict = {"appointment_number":1, "name":"Manas","age":35,"doctor":"optimetrist","doctorname":"Mr Laurent"}

    with open('doctor_appointment_database.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = appointment_table_header)
        # writer.writeheader()
        writer.writerow(new_appointment)


if __name__ == "__main__":
    port_number = 6969
    # Start the server on the port specified above
    app.run("localhost", port_number)