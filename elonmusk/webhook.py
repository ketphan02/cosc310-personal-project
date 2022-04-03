from flask import Flask, request, make_response
from flask_ngrok import run_with_ngrok
from main import cloud_function


app = Flask(__name__)
run_with_ngrok(app)
# route webhook and receive parameter named request


@app.route('/webhook', methods=['POST'])
def elon():
    return make_response(cloud_function(request.json))


if __name__ == '__main__':

    app.run()
