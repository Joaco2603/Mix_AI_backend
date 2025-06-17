from flask import Flask, request, jsonify
# Import dotenv and load enviroment variables
from dotenv import load_dotenv

# Routes
from llms.presentation.routes import mixer_bp

# Load enviroment variables to start of application
load_dotenv()

app = Flask(__name__)

# Register route mixer with blueprint
app.register_blueprint(mixer_bp)


if __name__ == '__main__':
    # Run flask.
    app.run(debug=True, host="0.0.0.0", port=5000)