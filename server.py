from flask import Flask, render_template
from cards import cards

app = Flask(__name__)

'''
# turno 1
red_jinja = Unit('Red Ninja', 3, 3, 7)
# turno 2
hard_alg = Unit('Hard Algorithm', 2, 'resistencia', 3)
hard_alg.play(red_jinja)

cards = [red_jinja, hard_alg]
'''


@app.route("/")
def hello_world():
    return render_template('index.html', cards=cards)


app.run()
