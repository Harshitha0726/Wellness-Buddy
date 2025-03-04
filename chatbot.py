import random
import spacy

nlp = spacy.load("en_core_web_sm")

health_data = {
    "headache": {
        "suggestions": [
            "For tension headaches, try a cold compress, warm shower, or OTC pain relievers. Manage stress and stay hydrated.",
            "Migraine sufferers, avoid triggers like certain foods or stress. Keep a headache diary. Rest in a dark, quiet room.",
            "Frequent or severe headaches? Consult a doctor. They may recommend medication or testing for underlying conditions.",
            "Neck tension can cause headaches. Gentle neck stretches and massages can help. Practice good posture."
        ],
        "patients": ["Neurologist", "General Physician", "Chiropractor"],
    },
    "cold": {
        "suggestions": [
            "Rest, stay hydrated, and use a humidifier. Warm liquids like tea or broth can soothe symptoms.",
            "OTC decongestants and pain relievers can help. Use saline nasal spray and gargle with salt water.",
            "Boost your immune system with vitamin C and zinc. See a doctor if symptoms worsen or last over 10 days.",
            "Honey can soothe a cough. Avoid close contact to prevent spreading the virus."
        ],
        "patients": ["General Physician", "Pulmonologist"],
    },
    "stomach ache": {
        "suggestions": [
            "Try the BRAT diet (bananas, rice, applesauce, toast). Avoid fatty or spicy foods. Sip clear fluids.",
            "A heating pad can relax abdominal muscles. Antacids can help with heartburn or indigestion.",
            "Seek immediate medical attention for severe pain, bloody stools, or persistent vomiting. These could be signs of serious conditions.",
            "Probiotics can help restore gut balance. Manage stress, as it can contribute to stomach issues."
        ],
        "patients": ["Gastroenterologist", "General Physician"],
    },
    "fever": {
        "suggestions": [
            "Monitor your temperature. Cool compresses and lukewarm baths can help. Stay hydrated.",
            "OTC fever reducers can lower your temperature. See a doctor for high or persistent fever.",
            "Rest in a cool, ventilated room. Avoid strenuous activity. Dress in light clothing.",
            "If you have chills, use a light blanket. Avoid sugary drinks and processed foods."
        ],
        "patients": ["General Physician", "Infectious Disease Specialist"],
    },
    "anxiety": {
        "suggestions": [
            "Practice deep breathing and mindfulness meditation. Identify and manage your triggers.",
            "Exercise and spend time in nature. Limit caffeine and alcohol.",
            "Consider therapy, like CBT. Connect with friends and family for support.",
            "Journaling can help track and manage anxiety. Explore relaxation techniques."
        ],
        "patients": ["Psychologist", "Psychiatrist", "Counselor"],
    },
    "insomnia": {
        "suggestions": [
            "Maintain a regular sleep schedule. Create a relaxing bedtime routine. Ensure your bedroom is dark and quiet.",
            "Avoid caffeine and alcohol before bed. Limit screen time. Try relaxation techniques.",
            "If insomnia persists, consult a doctor. They may recommend sleep studies or medication.",
            "Create a sleep-conducive environment. Use blackout curtains or earplugs. Optimize your mattress and pillows."
        ],
        "patients": ["Sleep specialist", "Psychiatrist", "General practitioner"],
    },
    "muscle pain": {
        "suggestions": [
            "Apply ice for the first 48 hours, then heat. Gentle stretching and massage can help. Use OTC pain relievers.",
            "Ensure you get enough magnesium and potassium. Stay hydrated. Practice good posture.",
            "Consider physical therapy for chronic pain. See a doctor for severe or persistent pain.",
            "Use a foam roller or massage ball. Light exercise can promote healing."
        ],
        "patients": ["Physiotherapist", "Orthopedic surgeon", "General practitioner"],
    },
    "allergies": {
        "suggestions": [
            "Identify and avoid triggers. Use OTC antihistamines or decongestants. Use saline nasal spray.",
            "Consult an allergist for severe allergies. They may recommend testing or immunotherapy.",
            "Monitor your symptoms and triggers. Carry an epinephrine auto-injector if needed.",
            "Keep your home clean and dust-free. Use hypoallergenic bedding."
        ],
        "patients": ["Allergist", "General Practitioner"],
    },
    "rash": {
        "suggestions": [
            "Avoid scratching. Apply a cold compress or calamine lotion. Wear loose clothing.",
            "Consult a dermatologist for severe rashes. They may recommend medication.",
            "Identify and avoid irritants or allergens. Keep skin moisturized.",
            "Avoid hot showers and baths. Use gentle cleansers."
        ],
        "patients": ["Dermatologist", "General practitioner"],
    },
    "indigestion": {
        "suggestions": [
            "Avoid spicy, fatty, or acidic foods. Eat smaller, more frequent meals. Drink herbal tea.",
            "OTC antacids can provide relief. Avoid lying down after eating.",
            "Manage stress, as it can worsen indigestion. Consult a doctor for persistent symptoms.",
            "Try ginger or peppermint to soothe your stomach. Keep a food diary to identify triggers."
        ],
        "patients": ["Gastroenterologist", "General Physician"],
    },
    "back pain": {
        "suggestions": [
            "Apply heat or ice. Gentle stretching and light exercise can help. Use OTC pain relievers.",
            "Practice good posture and lifting techniques. Consider physical therapy.",
            "Maintain a healthy weight. Use a supportive mattress and chair.",
            "If pain is severe or persistent, consult a doctor. They may recommend further testing or treatment."
        ],
        "patients": ["Orthopedic surgeon", "Physiotherapist", "General practitioner"],
    },
    "sore throat": {
        "suggestions": [
            "Gargle with warm salt water. Drink warm liquids like tea with honey. Use throat lozenges.",
            "Rest your voice. Use a humidifier. Avoid irritants like smoke.",
            "If the sore throat is severe or accompanied by fever, consult a doctor. It could be strep throat.",
            "Consume soft foods. Stay hydrated. Consider OTC pain relievers."
        ],
        "patients": ["General physician", "ENT specialist"],
    },
    "dizziness": {
        "suggestions": [
            "Sit or lie down immediately. Stay hydrated. Avoid sudden movements.",
            "Identify potential triggers like dehydration or low blood sugar. Consult a doctor for persistent dizziness.",
            "Manage stress. Get enough sleep. Avoid caffeine and alcohol.",
            "Practice balance exercises. Use a cane or walker if needed."
        ],
        "patients": ["Neurologist", "General physician", "Cardiologist"]
    }
}

def get_best_health_suggestion(user_input):
    """Provides the best possible health suggestion based on user input."""
    user_input = user_input.lower()
    best_match = None
    best_match_score = 0

    for key, data in health_data.items():
        if key in user_input:
            return random.choice(data["suggestions"])  # Exact match, return immediately

        # Calculate a simple match score (number of words in common)
        user_words = set(user_input.split())
        key_words = set(key.split())
        match_score = len(user_words.intersection(key_words))

        if match_score > best_match_score:
            best_match_score = match_score
            best_match = key

    if best_match:
        return random.choice(health_data[best_match]["suggestions"])
    else:
        return "I'm not able to provide specific medical advice for that input. Please consult a healthcare professional."

def get_best_patient_suggestion(user_input):
    """Provides the best possible patient suggestion based on user input."""
    user_input = user_input.lower()
    best_match = None
    best_match_score = 0

    for key, data in health_data.items():
        if key in user_input:
            return f"For this condition, you might consider consulting a {random.choice(data['patients'])}."

        user_words = set(user_input.split())
        key_words = set(key.split())
        match_score = len(user_words.intersection(key_words))

        if match_score > best_match_score:
            best_match_score = match_score
            best_match = key

    if best_match:
        return f"For this condition, you might consider consulting a {random.choice(health_data[best_match]['patients'])}."
    else:
        return "For general health concerns, a general physician is a good starting point."

def get_random_greeting():
    greetings = ["Hello!", "Hi there!", "Greetings!", "Welcome! How can I help you?"]
    return random.choice(greetings)

def get_random_farewell():
    farewells = ["Goodbye!", "Have a nice day!", "Take care!", "See you later!"]
    return random.choice(farewells)

def chatbot():
    print(f"Chatbot: {get_random_greeting()} How can I help you today?")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower() or "goodbye" in user_input.lower() or "exit" in user_input.lower():
            print("Chatbot:", get_random_farewell())
            break
        else:
            suggestion = get_best_health_suggestion(user_input)
            patient_suggestion = get_best_patient_suggestion(user_input)
            print("Chatbot:", suggestion)
            print("Chatbot:", patient_suggestion)

if __name__ == "__main__":
    chatbot()