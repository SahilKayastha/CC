from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from joblib import dump

# 1. Training data: questions and answers (bookstore support domain)
pairs = [
    ("hi", "Hello! Welcome to the bookstore. How may I help you?"),
    ("hello", "Hello! Welcome to the bookstore. How may I help you?"),
    ("what are your store hours", "We are open from 9am to 9pm every day."),
    ("where is the bookstore located", "We are located at 123 Main Street."),
    ("do you have any books on python programming", 
        "Yes, we have Python books. Check our Programming section."),
    ("what genres do you have", 
        "We have fiction, non-fiction, science, history, children's books, and more."),
    ("what is your return policy", 
        "You can return any book within 30 days of purchase with a receipt."),
    ("do you offer free shipping", "Yes, we offer free shipping on orders over $50."),
    ("how can i contact customer support", 
        "Email support@example.com or call (555) 123-4567."),
    ("thanks", "You're welcome! Do you need anything else?"),
    ("do you offer gift wrapping", "Yes, we offer free gift wrapping for all purchases.")
]
questions, answers = zip(*pairs)

# 2. Vectorize the questions with TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# 3. Train an SVM classifier (linear kernel for simplicity)
clf = SVC(kernel='linear')
clf.fit(X, answers)

# 4. Save the trained vectorizer and classifier to disk
dump((vectorizer, clf), "chatbot_model.joblib")

# 5. Interactive loop for user queries
print("Chatbot is ready! (type 'exit' or 'bye' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'bye']:
        print("Bot: Goodbye! Have a great day!")
        break
    # Transform the user input and predict the answer
    X_new = vectorizer.transform([user_input])
    response = clf.predict(X_new)[0]
    print("Bot:", response)
