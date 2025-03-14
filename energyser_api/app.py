from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
from flask_restful import Resource, Api

from config.db import db
from config.constant import LIEN_BASE_DE_DONNEES

from flask_migrate import Migrate
from flask_cors import CORS

from model.energyser import *
from resources.energyser import *

from resources.recommander import RecommendationApi


app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])

# Configuration du JWT et de la base de données
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

app.secret_key = os.urandom(24)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = LIEN_BASE_DE_DONNEES
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db.init_app(app) # Initialisation de db avec app

migrate = Migrate(app, db)
api = Api(app)

# Chargement des utilisateurs depuis le fichier CSV
# def load_users_from_csv():
#     users_df = pd.read_csv('path_to_your_csv/users.csv')
#     return users_df.to_dict(orient='records')



# # API pour gérer les utilisateurs
# class UserApi(Resource):
#     @jwt_required()
#     def get(self, route):
#         # Récupérer tous les utilisateurs
#         users = load_users_from_csv()
#         return jsonify(users)

#     @jwt_required()
#     def post(self, route):
#         # Ajouter un nouvel utilisateur à partir des données JSON
#         data = request.get_json()
#         users = load_users_from_csv()
#         new_user = {
#             "id": len(users) + 1,
#             "nom": data['nom'],
#             "email": data['email'],
#             "role": data['role'],
#             "created_at": pd.to_datetime('today').strftime('%Y-%m-%d')
#         }
#         users.append(new_user)
#         # Sauvegarder les données enrichies dans le CSV
#         pd.DataFrame(users).to_csv('path_to_your_csv/users.csv', index=False)
#         return jsonify(new_user)

#     @jwt_required()
#     def delete(self, route):
#         # Supprimer un utilisateur en fonction de son ID
#         users = load_users_from_csv()
#         user_id = route
#         users = [user for user in users if user["id"] != int(user_id)]
#         # Sauvegarder les données mises à jour dans le CSV
#         pd.DataFrame(users).to_csv('path_to_your_csv/users.csv', index=False)
#         return jsonify({"message": "User deleted successfully"})


# Route de test
@app.route('/a')    
def home():
    print('Trouvez Tous Officiel')
    # logger.info('FlotysHub')
    return render_template('index.html')

# API routes
# api.add_resource(UserApi, '/api/user/<string:route>', endpoint='all_user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(PropertiesApi, '/api/properties/<string:route>', endpoint='all_properties', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(RecommendationApi, '/api/recommend/<string:route>', endpoint='recommendations', methods=['GET', 'POST', 'DELETE', 'PATCH'])
# api.add_resource(DriversApi, '/api/drivers/<string:route>', endpoint='all_drivers', methods=['GET', 'POST', 'DELETE', 'PATCH'])


if __name__ == '__main__':
    app.run(debug=True)