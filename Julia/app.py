from flask import Flask, render_template, request, jsonify, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Campus directions with steps + images (static paths fixed)
campus_map = {
    "library": {
        "steps": [
            {
                "text": "From Main gate go left and walk 200 meters then go right.",
                "image": "picture/pathwalk2.jpg"
            },
            {
                "text": "Go straight and then go left again.",
                "image": "picture/Pathway5.jpg"
            },
            {
                "text": "And you will see the Albert Einstein Building.",
                "image": "picture/AlbertEinstein.jpg"
            },
            {
                "text": "Go inside and you will see the stairs on the left side.",
                "image": "picture/stairstolibrary.jpg"
            },
            {
                "text": "Go to the second floor and you see the entrance of the Library.",
                "image": "picture/infrontoflibrary.jpg"
            },
            {"text": "Go inside and enjoy reading."}
        ]
    },
    "gym": {
        "steps": [
            {
                "text": "From Main gate walk straight.",
                "image": "picture/AFter gate.jpg"
            },
            {
                "text": "Go left and walk 50 meters.",
                "image": "picture/pathwalk0.jpg"
            },
            {
                "text": "Go right and walk 25 meters.",
                "image": "picture/pathwalk3.jpg"
            },
            {
                "text": "Walk straight until you find the Gym Entrance.",
                "image": "picture/GymEntrance.jpg"
            },
            {
                "text": "Go inside and Enjoyyy.."
            }
        ]
    },
    "canteen": {
        "steps": [
            {
                "text": "Head towards the central plaza.",
                "image": "picture/canteen_step1.jpg"
            },
            {
                "text": "Walk beside the Student Center.",
                "image": "picture/canteen_step2.jpg"
            },
            {
                "text": "You have reached the canteen.",
                "image": "picture/canteen_final.jpg"
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
            # Convert image paths to full static URLs
            steps_with_static = []
            for step in campus_map[place]["steps"]:
                step_copy = step.copy()
                if "image" in step_copy:
                    step_copy["image"] = url_for("static", filename=step_copy["image"])
                steps_with_static.append(step_copy)

            return jsonify({
                "response": f"Here are the steps to reach the {place}:",
                "steps": steps_with_static
            })

    return jsonify({
        "response": "I don't know that location. Try: library, gym, canteen.",
        "steps": []
    })

if __name__ == "__main__":
    app.run(debug=True)
