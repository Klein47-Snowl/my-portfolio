from flask import Flask, jsonify, send_file
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def init_db():
    connection = sqlite3.connect("myfriends.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS friends (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            city TEXT
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM friends")
    if cursor.fetchone()[0] == 0:
        friends = [
            ("Thandi", 22, "Lusaka"),
            ("Mike", 24, "Kitwe"),
            ("Chipo", 21, "Ndola"),
            ("James", 23, "Livingstone")
        ]
        cursor.executemany("""
            INSERT INTO friends (name, age, city)
            VALUES (?, ?, ?)
        """, friends)

    connection.commit()
    connection.close()

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/api/friends")
def get_friends():
    connection = sqlite3.connect("myfriends.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM friends")
    rows = cursor.fetchall()
    connection.close()

    friends = []
    for row in rows:
        friends.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "city": row[3]
        })

    return jsonify(friends)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)