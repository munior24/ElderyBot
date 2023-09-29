# Ce code est utilisé pour remplir la base de données avec des données exemplaires afin de tester les fonctionnalités du chatbot.

import psycopg2
from datetime import date, time


# Sample data for three users: Antoine, Lucas, and Sarah
users_data = [
    {
        "first_name": "Antoine",
        "last_name": "Dupont",
        "age": 75,
        "gender": "Male",
        "room_number": "A101",
        "medical_conditions": "Hypertension",
        "allergies": "None",
        "caregiver_contact": "caregiver@example.com",
        "emergency_contact_name": "Marie Dupont",
        "emergency_contact_number": "1234567890"
    },
    {
        "first_name": "Lucas",
        "last_name": "Martin",
        "age": 80,
        "gender": "Male",
        "room_number": "B202",
        "medical_conditions": "Diabetes",
        "allergies": "Penicillin",
        "caregiver_contact": "caregiver@example.com",
        "emergency_contact_name": "Sophie Martin",
        "emergency_contact_number": "9876543210"
    },
    {
        "first_name": "Sarah",
        "last_name": "Johnson",
        "age": 70,
        "gender": "Female",
        "room_number": "C303",
        "medical_conditions": "Arthritis",
        "allergies": "Lactose",
        "caregiver_contact": "caregiver@example.com",
        "emergency_contact_name": "Michael Johnson",
        "emergency_contact_number": "4567890123"
    },
]

# Sample data for activities, meals, shower schedule, medications, appointments, and caregivers
activities_data = [
    {
        "activity_name": "Yoga",
        "description": "Morning yoga session for relaxation",
        "schedule_date": date(2023, 8, 2),
        "schedule_time": time(9, 30),
        "location": "Community Room",
        "user_id": 1,
    }
]

meals_data = [
    {
        "meal_name": "Breakfast",
        "description": "Scrambled eggs, toast, and orange juice",
        "meal_time": time(8, 0),
        "user_id": 1,
    }
]

shower_schedule_data = [
    {
        "schedule_date": date(2023, 8, 2),
        "schedule_time": time(10, 0),
        "user_id": 1,
    }
]

medications_data = [
    {
        "medication_name": "Aspirin",
        "dosage": "75mg",
        "schedule_date": date(2023, 8, 2),
        "schedule_time": time(11, 0),
        "user_id": 1,
    }
]

appointments_data = [
    {
        "appointment_type": "Doctor Checkup",
        "appointment_date": date(2023, 8, 3),
        "appointment_time": time(14, 30),
        "location": "Doctor's Clinic",
        "user_id": 1,
    }
]

caregivers_data = [
    {
        "caregiver_name": "John Smith",
        "phone": "1234567890",
        "email": "john.smith@example.com",
    }
]


def insert_data():
    try:
        # Connect to the database
        connection = psycopg2.connect(
            host="localhost",
            database="chatbot",
            user="postgres",
            password="mounir",
            port="5431"
        )
        # Get cursor
        cursor = connection.cursor()


        # Insert users data into the ElderlyUsers table
        for user_data in users_data:
            insert_query = """
            INSERT INTO ElderlyUsers (first_name, last_name, age, gender, room_number,
                                      medical_conditions, allergies, caregiver_contact,
                                      emergency_contact_name, emergency_contact_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data_tuple = (
                user_data["first_name"],
                user_data["last_name"],
                user_data["age"],
                user_data["gender"],
                user_data["room_number"],
                user_data["medical_conditions"],
                user_data["allergies"],
                user_data["caregiver_contact"],
                user_data["emergency_contact_name"],
                user_data["emergency_contact_number"],
            )
            cursor.execute(insert_query, data_tuple)
        print('users ok')
        # Insert activities data into the Activities table
        for activity_data in activities_data:
            insert_query = """
            INSERT INTO Activities (activity_name, description, schedule_date, schedule_time, location, user_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            data_tuple = (
                activity_data["activity_name"],
                activity_data["description"],
                activity_data["schedule_date"],
                activity_data["schedule_time"],
                activity_data["location"],
                activity_data["user_id"],
            )
            cursor.execute(insert_query, data_tuple)
        print('activity ok')
        # Insert meals data into the Meals table
        for meal_data in meals_data:
            insert_query = """
            INSERT INTO Meals (meal_name, description, meal_time, user_id)
            VALUES (%s, %s, %s, %s)
            """
            data_tuple = (
                meal_data["meal_name"],
                meal_data["description"],
                meal_data["meal_time"],
                meal_data["user_id"],
            )
            cursor.execute(insert_query, data_tuple)
        print('meals ok')
        # Insert shower schedule data into the ShowerSchedule table
        for shower_data in shower_schedule_data:
            insert_query = """
            INSERT INTO ShowerSchedule (schedule_date, schedule_time, user_id)
            VALUES (%s, %s, %s)
            """
            data_tuple = (
                shower_data["schedule_date"],
                shower_data["schedule_time"],
                shower_data["user_id"],
            )
            cursor.execute(insert_query, data_tuple)
        print('shower ok')
        # Insert medications data into the Medications table
        for medication_data in medications_data:
            insert_query = """
            INSERT INTO Medications (medication_name, dosage, schedule_date, schedule_time, user_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            data_tuple = (
                medication_data["medication_name"],
                medication_data["dosage"],
                medication_data["schedule_date"],
                medication_data["schedule_time"],
                medication_data["user_id"],
            )
            cursor.execute(insert_query, data_tuple)
        print('medication ok')
        # Insert appointments data into the Appointments table
        for appointment_data in appointments_data:
            insert_query = """
            INSERT INTO Appointments (appointment_type, appointment_date, appointment_time, location, user_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            data_tuple = (
                appointment_data["appointment_type"],
                appointment_data["appointment_date"],
                appointment_data["appointment_time"],
                appointment_data["location"],
                appointment_data["user_id"],
            )
            cursor.execute(insert_query, data_tuple)
        print('appointment ok')
        # Insert caregivers data into the Caregivers table
        for caregiver_data in caregivers_data:
            insert_query = """
            INSERT INTO Caregivers (caregiver_name, phone, email)
            VALUES (%s, %s, %s)
            """
            data_tuple = (
                caregiver_data["caregiver_name"],
                caregiver_data["phone"],
                caregiver_data["email"],
            )
            cursor.execute(insert_query, data_tuple)
        print('caregiver ok')
        # Commit the changes to the database
        connection.commit()
        print("Data inserted successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data:", error)
    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    insert_data()
