from flask import Flask, render_template, jsonify, make_response
import os

from conversion import int_to_kanji, kanji_to_int


app = Flask(__name__, static_folder='../dist/static', template_folder='../dist')

@app.route('/', defaults={'path': ''})


@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


@app.route('/v1/number2kanji/<number>')
def number2kanji(number=None):
    value = int_to_kanji(str(number))
    if value == 'error':
        return jsonify({
            'status': 'NG',
            'result': 'error'
        }), 204

    return jsonify({
        'status': 'OK',
        'result': value
    }), 200


@app.route('/v1/kanji2number/<kanji>')
def kanji2number(kanji=None):
    value = kanji_to_int(kanji)
    if value == 'error':
        return jsonify({
            'status': 'NG',
            'result': 'error'
        }), 204

    return jsonify({
        'status': 'OK',
        'result': value
    }), 200


if __name__ == '__main__':
    app.run()
