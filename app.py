from player import Player

def start():
    player1 = Player()
    player2 = Player()
    target = 50
    while player1.score < target and player2.score < target:
        player1.roll()
        player2.roll()
    if player1.score >= target:
        print("Player1 wins")
    elif player2.score >= target:
        print("Player2 wins")
    else:
        print("This is very very bad if you see this")

start()
result = "complete"

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return f'{result}'

if __name__ == '__main__':
    app.run(debug=True)
