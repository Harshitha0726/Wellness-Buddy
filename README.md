# Wellness Buddy - AI-Powered Health Chatbot

"Wellness Buddy" is an interactive, AI-driven health chatbot designed to provide users with quick and helpful information regarding common health concerns. It leverages natural language processing and a curated database of health suggestions to offer preliminary advice on symptoms.

## Features

* **Symptom-Based Suggestions:** Get relevant health suggestions and advice by inputting your symptoms.
* **Doctor Recommendations:** Receive suggestions on appropriate medical specialists to consult based on symptoms.
* **User-Friendly Web Interface:** Easy interaction with the chatbot through a clean and intuitive web interface built with Flask.
* **Responsive Design:** Accessible and visually appealing on various devices.
* **Dynamic Input Handling:** Capable of handling a wide range of user inputs and providing the best possible suggestion.
* **Keyword Matching:** Robust keyword-matching strategy for accurate responses.

## Technologies Used

* **Python:** Core programming language.
* **Flask:** Lightweight web framework for the user interface.
* **spaCy:** Natural language processing library for text analysis.
* **HTML/CSS/JavaScript:** Front-end development.
* **Jinja2:** Templating engine.

## Getting Started

### Prerequisites

* Python 3.6+
* pip

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd Wellness-Buddy
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    * **Windows:** `venv\Scripts\activate`
    * **macOS/Linux:** `source venv/bin/activate`

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Run the Flask application:**

    ```bash
    python interface.py
    ```

2.  **Open your web browser and navigate to** `http://127.0.0.1:5000/`.

## Future Enhancements

* Integration of more extensive medical databases.
* Improved natural language understanding.
* Personalized user profiles and health tracking.
* Voice interaction capabilities.
* Addition of more health conditions.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Disclaimer

This chatbot is intended for informational purposes only and should not replace professional medical advice. Always consult with a qualified healthcare provider for any health concerns.
