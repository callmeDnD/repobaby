from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from mangum import Mangum

app = Flask(__name__)
CORS(app)

# Campus directions with steps + images
campus_map = {
    "library": {
        "steps": [
            {
                "text": "From the main gate, walk straight for 200 meters.",
                "image": "/picture/library_step1.jpg"
            },
            {
                "text": "Turn left beside the Admin Building.",
                "image": "/picture/library_step2.jpg"
            },
            {
                "text": "The Library is the 2nd building on your right.",
                "image": "/picture/library_final.jpg"
            }
        ]
    },
    "gym": {
        "steps": [
            {
                "text": "From the canteen, walk straight ahead.",
                "image": "/picture/gym_step1.jpg"
            },
            {
                "text": "Continue for 5 minutes until you see the big dome.",
                "image": "/picture/gym_step2.jpg"
            },
            {
                "text": "You have reached the gym.",
                "image": "/picture/gym_final.jpg"
            }
        ]
    },
    "canteen": {
        "steps": [
            {
                "text": "Head towards the central plaza.",
                "image": "/picture/canteen_step1.jpg"
            },
            {
                "text": "Walk beside the Student Center.",
                "image": "/picture/canteen_step2.jpg"
            },
            {
                "text": "You have reached the canteen.",
                "image": "/picture/canteen_final.jpg"
            }
        ]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"].lower()

    for place in campus_map.keys():
        if place in user_input:
            return jsonify({
                "response": f"Here are the steps to reach the {place}:",
                "steps": campus_map[place]["steps"]
            })

    return jsonify({
        "response": "I don't know that location. Try: library, gym, canteen.",
        "steps": []
    })

if __name__ == "__main__":
    app.run(debug=True)
