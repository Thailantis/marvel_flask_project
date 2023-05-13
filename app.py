from flask import Flask
from marvel_api import app, routes

app = Flask(__name__)
app.config.from_dotenv()

if __name__ == '__main__':
    app.run(debug=True)
