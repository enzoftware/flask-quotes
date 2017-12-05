from flask import Flask , flash , redirect , render_template ,  request , session , abort

app = Flask(__name__)


@app.route("/")
def index():
    return "Index file"


'''
@app.route("/hello")
def hello():
    return "Hello world :v"
'''


@app.route("/members")
def members():
    return "Members"


'''
@app.route("/members/<string:name>/")  # The name of the param ,'name' in this case,be the same in the definition below
def getmember(name):
    return name
'''


@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

