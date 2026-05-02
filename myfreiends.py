from flask import Flask
import sqlite3

app = Flask(_name_)

@app.route("/")
def home():
    return"""
    <h1>Klein's Fkask App</h1>
    <a href='/friends'>See All friends</a>
    """

@app.route("/friends")
def friends():
    connection = sqlite3.connect("myfriends")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM friends")
    all_friends = cursor.fetchall()
    connection.close()

    html = "<h1>My friends</h1>" 
    for friend in all_friends:
        html += f"""
        <p>
            <b>{friend[1]}</b> - 
            Age: {friend[2]} -
            City: {friend[3]}
        </p>
        """
    return html
if _name_ == "_name_":
    app.run(debug=true)                  