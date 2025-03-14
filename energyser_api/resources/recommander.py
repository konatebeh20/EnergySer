# ressources/recommander.py

from flask_restful import Resource
from flask import request
from helpers.recommander import load_and_preprocess_data, calculate_similarity, recommend_similar_properties

class RecommendationApi(Resource):
    def get(self, route):
        if route == "recommend":
            property_id = request.args.get('property_id', type=int)
            recommendations = make_recommendation(property_id)
<<<<<<< HEAD
            return {'recommendations': recommendations}, 200
        
    def delete(self, route):
        if route == "delete_recommendation":
            # Logic to delete a recommendation
            return {"message": "Recommendation deleted"}, 200

    
            # # Charge et prétraite les données
            # data = load_and_preprocess_data()

            # # Calcule la similarité
            # similarity_matrix = calculate_similarity(data)

            # # Utilisez un ID de propriété donné pour la recommandation (par exemple, `property_id=0`)
            # property_id = int(request.args.get('property_id', 0))
            # recommendations = recommend_similar_properties(property_id, similarity_matrix)
            # # Retourner les propriétés similaires
=======

            return {'recommendations': recommendations}, 200
    
    # def get(self, route):
    #     if route == "recommend":
    #         return CreateProperties()

            # Charge et prétraite les données
            # data = load_and_preprocess_data()

            # Calcule la similarité
            # similarity_matrix = calculate_similarity(data)

            # Utilisez un ID de propriété donné pour la recommandation (par exemple, `property_id=0`)
            # property_id = int(request.args.get('property_id', 0))
            # recommendations = recommend_similar_properties(property_id, similarity_matrix)

            # Retourner les propriétés similaires
>>>>>>> b65ecaf194fac0bd8e8b0f53610f0592984a87fc
            # return {"recommendations": recommendations}
