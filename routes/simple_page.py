from flask import Blueprint, request
import jwt
import datetime

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


SECRET_KEY = "key"

@simple_page.route("/get-token", methods=['GET'])
def test():
        payload = {
                "user_id": 123,  # Example user data
                "role": "admin",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)  # Token valid for 1 hour
        } 
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token

@simple_page.route("/test-token", methods=['POST'])
def test2():
        body = request.json
        try:
                decoded = jwt.decode(body["token"], SECRET_KEY, algorithms=["HS256"])
                return "Decoded Payload: {decoded}"
        except jwt.ExpiredSignatureError:
                return "Token has expired"
        except jwt.InvalidTokenError:
                return "Invalid token"