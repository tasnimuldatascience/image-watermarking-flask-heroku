from flask import Flask

app = Flask(__name__)

# Ensure the ENV variable is set or default to 'development'
env = app.config.get("ENV", "development")  # Default to 'development' if ENV is not set

if env == "production":
    app.config.from_object("config.ProductionConfig")
elif env == "testing":
    app.config.from_object("config.TestingConfig")
else:  # Default to development if ENV is not set or invalid
    app.config.from_object("config.DevelopmentConfig")

from app import views
