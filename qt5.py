import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import webbrowser
from urllib.parse import urlencode

# Fonction pour générer les URLs de recherche Google et ouvrir le navigateur
def open_google_search():
    query = query_entry.text()
    keywords = keywords_entry.text()  # Récupère les mots clés supplémentaires
    num_results = int(results_entry.text() or 10)  # Nombre de résultats par page, par défaut 10
    num_pages = int(pages_entry.text() or 1)       # Nombre de pages, par défaut 1
    
    if query:
        full_query = f"{query} {keywords}"  # Combine la requête principale avec les mots clés
        for page in range(num_pages):
            start_index = page * num_results  # Calculer le point de départ pour chaque page
            # Paramètres de la recherche
            params = {
                "q": full_query,
                "hl": "fr",   # Langue des résultats
                "gl": "fr",   # Pays des résultats
                "num": num_results,  # Nombre de résultats par page
                "start": start_index # Point de départ pour la pagination
            }
            # Encode les paramètres pour l'URL
            url_params = urlencode(params)
            # URL de recherche Google
            google_url = f"https://www.google.com/search?{url_params}"
            # Ouvre l'URL dans le navigateur par défaut
            webbrowser.open(google_url, new=2)  # `new=2` pour ouvrir dans une nouvelle fenêtre

# Configuration de l'interface PyQt5
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Google Search Opener")

# Création des widgets
layout = QVBoxLayout()

layout.addWidget(QLabel("Recherche principale:"))
query_entry = QLineEdit()
layout.addWidget(query_entry)

layout.addWidget(QLabel("Mots clés supplémentaires:"))
keywords_entry = QLineEdit()
layout.addWidget(keywords_entry)

layout.addWidget(QLabel("Nombre de résultats par page (1-100):"))
results_entry = QLineEdit()
layout.addWidget(results_entry)

layout.addWidget(QLabel("Nombre de pages:"))
pages_entry = QLineEdit()
layout.addWidget(pages_entry)

search_button = QPushButton("Search")
search_button.clicked.connect(open_google_search)
layout.addWidget(search_button)

window.setLayout(layout)

# Affichage de la fenêtre
window.show()
sys.exit(app.exec_())
