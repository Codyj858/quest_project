from .extensions import db, migrate
from flask import Flask
from config import DevelopmentConfig, TestingConfig, ProductionConfig

def create_app(config_name):
    app = Flask(__name__)
    if config_name == "development":
        app.config.from_object(DevelopmentConfig) 
    elif config_name == "testing":
        app.config.from_object(TestingConfig)
    elif config_name == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    print("DB URL:", app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import quests_bp
    app.register_blueprint(quests_bp)

    return app