from flask import Flask , flash , redirect , render_template ,  request , session , abort
from random import  choice
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
    quotes = [
        "\"If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.\" -- John Louis von Neumann ",
        "\"Computer science is no more about computers than astronomy is about telescopes\" --  Edsger Dijkstra ",
        "\"To understand recursion you must first understand recursion..\" -- Unknown",
        "\"You look at things that are and ask, why? I dream of things that never were and ask, why not?\" -- Unknown",
        "\"Mathematics is the key and door to the sciences.\" -- Galileo Galilei",
        "\"Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.\" -- Unknown"]

    gifs = [
        "https://i.pinimg.com/originals/94/49/b1/9449b1834ba649db8a675519238d8e77.gif",
        "https://78.media.tumblr.com/ee98da65020e4ffc89c29b2f30f810b8/tumblr_o3dikz274b1upf2pto1_400.gif",
        "https://media1.tenor.com/images/9190e0d5f2fb568957ff0a97f143611f/tenor.gif?itemid=3433814",
        "https://i.pinimg.com/originals/f7/ae/07/f7ae074d3682002ae56ce6ce04108e7d.gif",
        "https://media1.tenor.com/images/efc9f6ce8923eadf351b676f29bf943c/tenor.gif?itemid=5449984",
        "http://teamjimmyjoe.com/wp-content/uploads/2016/11/trump-clinton-godzilla-funny-gifs.gif"
    ]
    
    quote = choice(quotes)
    gif_url = choice(gifs)
    print(gif_url)

    return render_template(
        'test.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

