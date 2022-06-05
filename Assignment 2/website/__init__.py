from flask import *

def create_app():
    app=Flask(__name__)
    app.debug=True 

    from .views import mybp
    app.register_blueprint(mybp)
    
    return app
