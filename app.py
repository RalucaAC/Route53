from flask import Flask

app = Flask(__name__)

@app.route('/') 
#Later on here we can paste the URL of our Route
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')

