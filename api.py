from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def page():
    return render_template('index.html')

app.run(host='0.0.0.0')