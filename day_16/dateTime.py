# 🟢 Exercices: Jour 16 - Python Datetime

# 1. Importation des modules nécessaires
from datetime import datetime, date, timedelta

# 2. Exercice 1: Obtenir les composants de date et d'heure actuels

current_datetime = datetime.now()
print(f"Date et heure actuelles: {current_datetime}")
print(f"Jour actuel: {current_datetime.day}")
print(f"Mois actuel: {current_datetime.month}")
print(f"Année actuelle: {current_datetime.year}")
print(f"Heure actuelle: {current_datetime.hour}")
print(f"Minutes actuelles: {current_datetime.minute}")
print(f"Timestamp actuel: {current_datetime.timestamp()}")

# 3. Exercice 2: Formater la date actuelle
formatted_date = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Date formatée (MM/JJ/AAAA, HH:MM:SS): {formatted_date}")

# 4. Exercice 3: Conversion de chaîne en datetime
date_string = "5 December, 2019"
converted_date = datetime.strptime(date_string, "%d %B, %Y")
print(f"Chaîne d'origine: {date_string}")
print(f"Date convertie: {converted_date}")

# 5. Exercice 4: Temps restant jusqu'au Nouvel An
today = date.today()
next_year = today.year + 1
new_year = date(next_year, 1, 1)
days_until_new_year = (new_year - today).days
print(f"Aujourd'hui: {today}")
print(f"Prochain jour de l'An: {new_year}")
print(f"Jours jusqu'au Nouvel An: {days_until_new_year}")

# 6. Exercice 5: Temps écoulé depuis l'epoch Unix
epoch = datetime(1970, 1, 1)
time_since_epoch = current_datetime - epoch
print(f"Date/Heure actuelle: {current_datetime}")
print(f"Epoch Unix: {epoch}")
print(f"Jours écoulés depuis l'epoch Unix: {time_since_epoch.days}")

# 7. Exercice 6: Cas d'utilisation du module datetime
print("1. Journalisation des événements avec horodatage")
print("2. Planification des tâches et rappels")
print("3. Calcul de l'âge à partir de la date de naissance")
print("4. Mesure du temps d'exécution du code")
print("5. Création de comptes à rebours")
print("6. Gestion des fuseaux horaires dans les applications")
print("7. Définition des dates d'expiration pour le contenu")
print("8. Analyse des séries temporelles")
print("9. Création d'applications de calendrier")
print("10. Suivi de la durée des sessions utilisateur")
