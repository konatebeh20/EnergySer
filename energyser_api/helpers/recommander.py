# helpers/recommander.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
from model.energyser import Properties
from config.db import db


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

<<<<<<< HEAD
# # Fonction pour récupérer les propriétés de la base de données
# def get_properties_from_db():
#     properties = Properties.query.all()
#     property_data = []

#     # Récupérer les propriétés de la base de données et ajouter leurs données dans la liste
#     for prop in properties:
#         property_data.append([
#             prop.global_active_power,
#             prop.global_reactive_power,
#             prop.voltage,
#             prop.global_intensity
#         ])
    
#     return pd.DataFrame(property_data)

=======
>>>>>>> b65ecaf194fac0bd8e8b0f53610f0592984a87fc

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


<<<<<<< HEAD

# Fonction principale pour effectuer la recommandation et enregistrer les données
def make_recommendation(property_id):
    dataset_data = load_and_preprocess_data()
    db_data = get_properties_from_db()  # Récupérer les propriétés de la DB

    # Combine les données du dataset et de la DB
=======
# Fonction principale pour effectuer la recommandation
def make_recommendation(property_id):
    # Charger et prétraiter les données
    dataset_data = load_and_preprocess_data()
    
    # Récupérer les propriétés de la base de données
    db_data = get_properties_from_db()

    # Combiner les données de la base de données et du dataset
>>>>>>> b65ecaf194fac0bd8e8b0f53610f0592984a87fc
    combined_data = pd.concat([dataset_data[['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity']], db_data], ignore_index=True)

    # Calculer la similarité
    similarity_matrix = calculate_similarity(combined_data)

<<<<<<< HEAD
    # Récupérer les recommandations
    recommendations = recommend_similar_properties(property_id, similarity_matrix)

    # Enregistrer les recommandations dans la base de données et dans un fichier CSV
    save_recommendations_to_db(property_id, recommendations)
    save_recommendations_to_csv(recommendations)

    return recommendations


# Fonction pour sauvegarder les recommandations dans la base de données
def save_recommendations_to_db(property_id, recommendations):
    for recommended_property in recommendations:
        recommended_property_id = recommended_property[0]
        similarity_score = recommended_property[1]

        # Crée un enregistrement pour chaque recommandation
        recommendation = PropertyRecommendation(property_id=property_id, recommended_property_id=recommended_property_id, similarity_score=similarity_score)
        db.session.add(recommendation)
    db.session.commit()


# Fonction pour sauvegarder les recommandations dans un fichier CSV
def save_recommendations_to_csv(recommendations):
    recommendations_data = []
    for recommended_property in recommendations:
        recommended_property_id = recommended_property[0]
        similarity_score = recommended_property[1]
        recommendations_data.append([recommended_property_id, similarity_score])

    recommendations_df = pd.DataFrame(recommendations_data, columns=['PropertyID', 'SimilarityScore'])
    recommendations_df.to_csv('EnergySer/energyser_api/data/electricity_recommendations.csv', mode='a', header=False, index=False)
=======
    # Récupérer les recommandations pour la propriété donnée
    recommendations = recommend_similar_properties(property_id, similarity_matrix)

    return recommendations
>>>>>>> b65ecaf194fac0bd8e8b0f53610f0592984a87fc
