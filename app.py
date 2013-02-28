# encoding: utf-8
import os

from flask import Flask, render_template, request

from rotate import mirror, rotate, transpose

app = Flask(__name__)

@app.route('/')
@app.route('/rotate', methods=['GET', 'POST'])
def r():
    options = {
        'rotation': [('positive', 'Counterclockwise'), ('negative', 'Clockwise')],
        'iterations': [(i, u'%s°' % (90*i)) for i in range(1, 4)],
    }
    text = output = ''
    mode = 'rotate'

    def parse_form(text):
        iterations = int(request.form['iterations'])
        clockwise = request.form['rotation'] == 'negative'
        return do_rotate(text, iterations, clockwise=clockwise)

    def do_rotate(mytext, iterations, clockwise=False):
        if clockwise:
            # Subtract from 360 degree rotation in other direction
            iterations = 4 - iterations
        for _ in range(iterations):
            mytext = rotate(mytext)
        return mytext

    if request.method == 'POST':
        text = request.form['text']
        output = parse_form(text)

    return render_template('submit.html', mode=mode, options=options, text=text, output=output)


@app.route('/mirror', methods=['GET', 'POST'])
def m():
    options = {
        'axis': [('h', 'Horizontal'), ('v', 'Vertical')],
    }
    text = output = ''
    mode = 'mirror'

    def parse_form(text):
        vertical_axis = request.form['axis'] == 'v'
        return mirror(text, vertical=vertical_axis)

    if request.method == 'POST':
        text = request.form['text']
        output = parse_form(text)

    return render_template('submit.html', mode=mode, options=options, text=text, output=output)


@app.route('/transpose', methods=['GET', 'POST'])
def t():
    options = {}
    text = output = ''
    mode = 'transpose'

    def parse_form(text):
        return transpose(text)

    if request.method == 'POST':
        text = request.form['text']
        output = parse_form(text)

    return render_template('submit.html', mode=mode, options=options, text=text, output=output)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
