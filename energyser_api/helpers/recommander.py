# helpers/recommander.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime


# Fonction pour charger les données et les prétraiter
def load_and_preprocess_data():
    # Charger le fichier CSV
    file_path = 'EnergySer/energyser_api/data/household_power_consumption.csv'
    data = pd.read_csv(file_path, delimiter=',')

    # Conversion des colonnes en formats appropriés
    data['Date'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])
    data.set_index('Date', inplace=True)
    data.drop(columns=['Time'], inplace=True)

    # Gérer les valeurs manquantes
    data.fillna(method='ffill', inplace=True)

    # Normalisation des données
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity']])
    data[['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity']] = scaled_data

    return data


# Fonction pour calculer la similarité entre les propriétés basées sur la consommation d'énergie
def calculate_similarity(data):
    # Calcul de la similarité cosinus entre les propriétés
    similarity_matrix = cosine_similarity(data[['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity']])
    return similarity_matrix


# Fonction pour recommander des propriétés similaires
def recommend_similar_properties(property_id, similarity_matrix):
    # Trouver les propriétés les plus similaires
    similar_properties = list(enumerate(similarity_matrix[property_id]))
    similar_properties = sorted(similar_properties, key=lambda x: x[1], reverse=True)

    # Retourner les 5 propriétés les plus similaires
    return similar_properties[1:6]  # Exclut la propriété elle-même


# Fonction principale pour effectuer la recommandation
def make_recommendation(property_id):
    # Charger et prétraiter les données
    dataset_data = load_and_preprocess_data()
    
    # Récupérer les propriétés de la base de données
    db_data = get_properties_from_db()

    # Combiner les données de la base de données et du dataset
    combined_data = pd.concat([dataset_data[['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity']], db_data], ignore_index=True)

    # Calculer la similarité
    similarity_matrix = calculate_similarity(combined_data)

    # Récupérer les recommandations pour la propriété donnée
    recommendations = recommend_similar_properties(property_id, similarity_matrix)

    return recommendations