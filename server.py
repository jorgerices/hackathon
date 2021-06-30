from flask import Flask, render_template, flash
from cards import *


app = Flask(__name__, static_folder='./static')
app.secret_key = 'asdasdasffasf'

cardsToShow = []
'''
cards = [hardAlgorithm, promise, pairProgramming, Red_Jinja, Black_Jinja]

1	El jugador 1 convoca a "Ninja Cinturón Rojo"   Jugada1()
1	El jugador 1 juega "Algoritmo duro" en "Ninja Cinturón Rojo" Jugada2()
(en este caso la carta Ninja Cinturón Rojo ve modificada su resistencia)

2	El jugador 2 convoca a "Ninja Cinturón Negro"Jugada3()
2	El jugador 2 juega "Rechazo de promesa no controlada" en "Ninja Cinturón Rojo" Jugada4()
(en este caso la carta Ninja Cinturón Rojo ve modificada su resistencia)

3	El jugador 1 juega "Programación en pareja" en "Ninja Cinturón Rojo" Jugada5()
(en este caso la carta Ninja Cinturón Rojo ve modificada su fuerza)
3	El jugador 1 juega el ataque "Ninja Cinturón Rojo" "Ninja Cinturón Negro" Jugada7()
(en este caso la carta Ninja Cinturón Negro ve disminuida su resistencia)  Jugada8()
'''

# Effect Cards
hardAlgorithm = Effect('Hard Algorithm', 2, "Increase target's resistance by 3", 'res', 3, 'https://media.makeameme.org/created/algorithms-5ca443.jpg')
promise = Effect('Promise', 1, "Reduce target's resistance by 2", 'res', -2, 'https://media.makeameme.org/created/i-promise-jmjjcy.jpg')
pairProgramming = Effect('Pair Programming', 3, "Increase target's power by 2", 'power', 2, "https://cdn.hackernoon.com/hn-images/1*zRrkoarX94CUZe3-NrSYGg.png")

# Unit Cards
Red_Jinja=Unit("Red Ninja", 3,3,4,"https://www.karatemart.com/images/products/large/red-ninja-uniform-800583.jpg")
Black_Jinja=Unit("Black Ninja",4,5,4,"https://pbs.twimg.com/profile_images/1336354559048880129/yIQSfFLy_400x400.jpg")

# All cards list
cards = [hardAlgorithm, promise, pairProgramming, Red_Jinja, Black_Jinja]

def resetCards():
    hardAlgorithm = Effect('Hard Algorithm', 2, "Increase target's resistance by 3", 'res', 3, 'https://media.makeameme.org/created/algorithms-5ca443.jpg')
    promise = Effect('Promise', 1, "Reduce target's resistance by 2", 'res', -2, 'https://media.makeameme.org/created/i-promise-jmjjcy.jpg')
    pairProgramming = Effect('Pair Programming', 3, "Increase target's power by 2", 'power', 2, "https://cdn.hackernoon.com/hn-images/1*zRrkoarX94CUZe3-NrSYGg.png")
    Red_Jinja=Unit("Red Ninja", 3,3,4,"https://www.karatemart.com/images/products/large/red-ninja-uniform-800583.jpg")
    Black_Jinja=Unit("Black Ninja",4,5,4,"https://pbs.twimg.com/profile_images/1336354559048880129/yIQSfFLy_400x400.jpg")
    cards = [hardAlgorithm, promise, pairProgramming, Red_Jinja, Black_Jinja]

def jugada1():
    cardsToShow.clear()
    cardsToShow.append(Red_Jinja)
    cardsToShow.append(hardAlgorithm)
    return 'Jugador 1 usa Algoritmo en Ninja Cinturón Rojo'

def jugada2():
    cardsToShow.clear()
    hardAlgorithm.useEffect(Red_Jinja)
    cardsToShow.append(Red_Jinja)
    return 'Ninja Rojo ha aumentado su resistencia en: 3'

def jugada3():
    cardsToShow.clear()
    cardsToShow.append(Black_Jinja)
    cardsToShow.append(promise)
    return 'Jugador 2 usa Promesa en Ninja Rojo'

def jugada4():
    cardsToShow.clear()
    promise.useEffect(Red_Jinja)
    cardsToShow.append(Red_Jinja)
    return 'Ninja Rojo ha modificado su resistencia en: -2'

def jugada5():
    cardsToShow.clear()
    cardsToShow.append(pairProgramming)
    cardsToShow.append(Red_Jinja)
    return 'Jugador 1 usa Programación en Pareja en Ninja Cinturón Rojo'

def jugada6():
    cardsToShow.clear()
    pairProgramming.useEffect(Red_Jinja)
    cardsToShow.append(Red_Jinja)
    return 'Ninja Rojo ha incremetado su poder en: 2'

def jugada7():
    cardsToShow.clear()
    cardsToShow.append(Red_Jinja)
    cardsToShow.append(Black_Jinja)
    return 'jugador 1 ataca al Ninja Negro con su Ninja Rojo'

def jugada8():
    cardsToShow.clear()
    Red_Jinja.attack(Black_Jinja)
    cardsToShow.append(Black_Jinja)
    return 'Jugar 1 ha ganado!!! \n JUEGO TERMINADO'

# Ingresar una alerta de que ha terminado el juego

jugadas=[jugada1,jugada2,jugada3,jugada4,jugada5,jugada6,jugada7, jugada8]

app.sgte_jugada = 0

@app.route("/")
def hello_world():
    if app.sgte_jugada < len(jugadas):
        message = jugadas[app.sgte_jugada]()
        if message is not None:
            flash(message)
        if app.sgte_jugada == 7:
            app.sgte_jugada = 0
        else:
            app.sgte_jugada +=1
        return render_template('index.html', cards=cardsToShow)

app.run()
