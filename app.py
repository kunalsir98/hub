from flask import Flask,render_template,redirect,abort
from apps import APPS

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apps')
def apps():
    return render_template('apps.html',apps=APPS)

@app.route("/launch/<app_key>")
def launch_app(app_key):
    app_data = APPS.get(app_key)
    if not app_data:
        abort(404)
    return redirect(app_data["url"])


if __name__ == "__main__":
    app.run(debug=True)