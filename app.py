from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Fonction de réponse du chatbot
def chatbot_response(message):
    message = message.lower()  # Convertir le message en minuscules
    if "bonjour" in message:
        return "Bonjour Fredo! Comment puis-je t'aider?"
    elif "welcom" in message:
        return "Je suis désolé mais les welcoms, c'est non. Tu en as fais assez."
    elif "merci" in message:
        return "De rien Fredo! Si tu as besoin de rien n'hésite surtout pas!😊"
    elif "eva" in message:
        return "C'est vraiment une personne géniale, tu trouves pas ?"
    elif "véhicule utilitaire" in message:
        return "Non. Je ne veux plus jamais en entendre parler."
    elif "peap" in message:
        return "PEAP ou CBM, on y comprend rien à tes offres..."
    elif "chat" in message:
        return "Je crois que tes filles veulent que tu adoptes un chat"
    else:
        return "Je ne comprends pas encore cette question. Pouvez-vous reformuler ?"


# Route principale pour interagir avec le chatbot
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':  # Si la méthode est POST
        user_input = request.json.get('message')  # Récupère le message envoyé
        response = chatbot_response(user_input)  # Génère une réponse
        return jsonify({"response": response})  # Retourne la réponse au format JSON
    else:  # Si la méthode est GET
        return "Cette route accepte uniquement les requêtes POST avec un message JSON."

# Ajouter une page d'accueil (facultatif)
@app.route('/')
def home():
    return "Bienvenue sur mon chatbot ! Utilisez /chat pour interagir."

if __name__ == '__main__':
    # Pour le déploiement sur un serveur en ligne (par exemple, Railway)
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))


