import os
from flask import Flask
from pymongo import MongoClient
from routes import pages


def create_app():
    app = Flask(__name__)
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
    )

    #double check how to get this working
    client = MongoClient("MONGODB_URI")
    app.db = client.watchlist

    app.register_blueprint(pages)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)