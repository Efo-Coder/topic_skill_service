# Importieren von Modulen für Webentwicklung (Flask) und Dateiverwaltung
import os
from flask import Flask, jsonify
from data_manager import JsonDataManager  # Import der selbst erstellten Klasse


app = Flask(__name__) # Erstelle eine Flask-Anwendung
data_manager = JsonDataManager() # Instanz des JSON-Datenmanagers

# Definition des Pfads zum Verzeichnis, in dem die Daten gespeichert sind
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# Pfad zur Datei mit den Themen (topics)
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')

# Route für die Startseite der Anwendung
@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

# Route für das Abrufen der Themenliste im JSON-Format
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE)  # Lese Themen aus der Datei
    return jsonify(topics)  # Rückgabe als JSON-Antwort

# Starte die Flask-Anwendung im Debug-Modus auf Port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)