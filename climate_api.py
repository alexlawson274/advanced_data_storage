# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

Stations= [{"city": "Waikiki", "ave_temp": "71.4"},
    {"city": "Kaneohe", "ave_temp": "74.5"},
    {"city": "Kualoa", "ave_temp": "70.3"},
    {"city": "Pearl City", "ave_temp": "75.6"},
    {"city": "Upper Wahaiwa", "ave_temp": "70.3"},
    {"city": "Waihee", "ave_temp": "68.6"},
    {"city": "Honolulu", "ave_temp": "74.5"}]

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return Stations


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)