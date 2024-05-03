import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# adding the data to firebase storage bucket
cred = credentials.Certificate("serviceAccountKey.json")
# putting the database url in json format
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognisation-e310a-default-rtdb.firebaseio.com/"
})

# reference path of the database
ref = db.reference('Students')
# adding data in json format
data = {
    "321654":  # ----> Key
        {      # ----> Value
            "name": "Arnab Adhikary",
            "major": "Computer Engineering",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-01-11 00:54:34"
        },
    "852741":
        {
            "name": "Guido van Rossum",
            "major": "Computer Engineering with AI",
            "starting_year": 1991,
            "total_attendance": 12,
            "standing": "O",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}
# send the data
for key, value in data.items():
    ref.child(key).set(value)
