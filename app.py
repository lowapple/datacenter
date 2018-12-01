from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome DayTour data center'

if __name__ == '__main__':
    app.run(debug=True)

