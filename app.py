from flask import Flask, request, render_template, redirect, url_for, abort

import game

app = Flask(__name__)


@app.route('/')
def hello():
    return '메인페이지'

@app.route('/hello/')
    return 'Hello.  World!'
    

@app.route('/hello/<name>')
def hellovar(name):
  charact =game.set_charact(name)
  return "{0}님 반갑습니다. (HP {1}으로 게임을 시작 합니다" .format(character["name"], character["hp"]))

@app.route('/input/<int:num>/')
def input_num(num):ff
        if num == 1:
            return "도라에몽"
        elif num == 2:
            return "진구"
        elif num == 3:
            return "퉁퉁이"
        elif num == 4:
            return "없어요"


if __name__ == '__main__':
        app.run(debug=True)