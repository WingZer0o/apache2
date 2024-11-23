from flask import Blueprint, request, current_app, jsonify
import jwt
import os
import datetime

jwt_print = Blueprint('jwt_print', __name__)



@jwt_print.route("/get-token", methods=['GET'])
def test():
        payload = {
                "user_id": 123,  # Example user data
                "role": "admin",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)  # Token valid for 1 hour
        }
        key_path = os.path.join(current_app.root_path, 'routes', 'jwt', 'certs', 'yourdomain-private.pem')
        jwt_private_key = open(key_path, "r")
        token = jwt.encode(payload, jwt_private_key.read(), algorithm="RS256")
        return jsonify({'token': token}), 200

@jwt_print.route("/test-token", methods=['POST'])
def test2():
        body = request.json
        try:
                key_path = os.path.join(current_app.root_path, 'routes', 'jwt', 'certs', 'yourdomain-public.pem')
                jwt_public_key = open(key_path, "r")
                decoded = jwt.decode(body["token"], jwt_public_key.read(), algorithms=["RS256"])
                return "Decoded Payload: {decoded}"
        except jwt.ExpiredSignatureError:
                return "Token has expired"
        except jwt.InvalidTokenError:
                return "Invalid token"