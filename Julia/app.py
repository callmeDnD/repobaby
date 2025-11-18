from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary of campus locations and directions
campus_map = {
    "library": "From the main gate, walk straight for 200 meters and turn left beside the Admin Building. The Library is the 2nd building on your right.",
    "gym": "The gym is located near the Sports Complex. From the canteen, walk straight ahead for 5 minutes until you see the big dome-shaped building.",
    "canteen": "From any classroom building, head towards the central plaza. The canteen is beside the Student Center.",
    "registrar": "The Registrar’s Office is on the ground floor of the Administration Building near the main entrance.",
    "clinic": "The campus clinic is behind the Science Building, next to the parking area."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"].lower()

    # Loop through dictionary keys (campus_map) to find a match
    for place in campus_map.keys():
        if place in user_input:
            return jsonify({"response": f"Here's how to get to the {place}: {campus_map[place]}"})

    # Default response if place not found
    return jsonify({"response": "I'm sorry, I don't know that location. Try asking about the library, gym, canteen, registrar, or clinic."})

if __name__ == "__main__":
    app.run(debug=True)
