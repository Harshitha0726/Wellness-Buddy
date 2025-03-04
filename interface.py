# interface.py (Flask interface)
from flask import Flask, render_template, request, jsonify
import chatbot  # Import your chatbot functions

app = Flask(__name__)

@app.route("/")
def index():
    greeting = chatbot.get_random_greeting()
    return render_template("index.html", greeting=greeting)

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]

    if "bye" in user_input.lower() or "goodbye" in user_input.lower() or "exit" in user_input.lower():
        bot_response = chatbot.get_random_farewell()
    else:
        suggestion = chatbot.get_best_health_suggestion(user_input)
        patient_suggestion = chatbot.get_best_patient_suggestion(user_input)
        bot_response = suggestion + "\n" + patient_suggestion

    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)