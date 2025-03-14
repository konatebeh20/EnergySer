# ressources/recommander.py

from flask_restful import Resource
from flask import request
from helpers.recommander import load_and_preprocess_data, calculate_similarity, recommend_similar_properties

class RecommendationApi(Resource):
    def get(self, route):
        if route == "recommend":
            # Charge et prétraite les données
            data = load_and_preprocess_data()

            # Calcule la similarité
            similarity_matrix = calculate_similarity(data)

            # Utilisez un ID de propriété donné pour la recommandation (par exemple, `property_id=0`)
            property_id = int(request.args.get('property_id', 0))
            recommendations = recommend_similar_properties(property_id, similarity_matrix)

            # Retourner les propriétés similaires
            return {"recommendations": recommendations}
