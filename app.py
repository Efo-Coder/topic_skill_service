import os
from flask import Flask, jsonify
from data_manager import JsonDataManager


app = Flask(__name__) # Erstelle eine Flask-Anwendung
data_manager = JsonDataManager() # Instanz des JSON-Datenmanagers

# Definition des Pfads zum Verzeichnis, in dem die Daten gespeichert sind
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# Pfad zur Datei mit den Themen (topics)
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')
SKILLS_FILE = os.path.join(DATA_DIR, 'skills.json')

# Route für die Startseite der Anwendung
@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

# Route für das Abrufen der Themenliste im JSON-Format
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE)  # Lese Themen aus der Datei
    return jsonify(topics)  # Rückgabe als JSON-Antwort

@app.route('/skills', methods=['GET'])
def get_skills():
    skills = data_manager.read_data(SKILLS_FILE) 
    return jsonify(skills)

@app.route('/topics/<id>', methods=['GET'])
def get_topic_by_id(id):
    topics = data_manager.read_data(TOPICS_FILE)
    topic = next((topic for topic in topics if topic.get('id').lower() == id.lower()), None)
    if topic:
        return jsonify(topic)
    else:
        return jsonify({"error": "Topic not found."}), 404


@app.route('/skills/<id>', methods=['GET'])
def get_skill_by_id(id):
    skills = data_manager.read_data(SKILLS_FILE)
    skill = next((skill for skill in skills if skill.get('id').lower() == id.lower()), None)
    if skill:
        return jsonify(skill)
    else:
        return jsonify({"error": "Skill not found."}), 404

# Starte die Flask-Anwendung im Debug-Modus auf Port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)