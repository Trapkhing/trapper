from flask import Flask
app = Flask(__name__, static_folder='templates', static_url_path='')
@app.route('/')
def trap():
    return app.send_static_file('trap.html')
@app.route("/about")
def about():
    return app.send_static_file ("about.html")
if __name__ == '__main__':
    app.run()