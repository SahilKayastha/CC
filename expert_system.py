# Define a dictionary of common symptoms and advice
medical_dict = {
    "fever": "Take rest, stay hydrated, and consult a doctor if temperature is very high.",
    "cough": "Use cough syrup and drink warm fluids. Visit doctor if persists.",
    "headache": "Take a painkiller and rest. Seek medical help if severe.",
    "chest pain": "Seek immediate medical attention!",
    "stomach ache": "Eat light food. Visit hospital if pain continues.",
    "fracture": "Immobilize the area and rush to the emergency room."
}

# Function to handle user queries
def handle_query(symptom):
    if symptom.lower() == "exit":
        return "Goodbye! Stay healthy!"
    elif symptom.lower() in medical_dict:
        return medical_dict[symptom.lower()]
    else:
        return "I'm sorry, please visit the hospital for proper diagnosis."

# Main loop
print("Welcome to Hospital Help Desk! (Type 'exit' to quit)")
while True:
    symptom = input("Describe your symptom: ")
    response = handle_query(symptom)
    print("Advice:", response)
    if symptom.lower() == "exit":
        break
