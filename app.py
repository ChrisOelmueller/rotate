# encoding: utf-8
import os

from flask import Flask, render_template, request

from rotate import mirror, rotate, transpose

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def r():
    options = {
        'operation': [(x, x.capitalize()) for x in ('rotate', 'mirror', 'transpose')],
        'rotation': [('positive', 'Counterclockwise'), ('negative', 'Clockwise')],
        'iterations': [(i, u'%s°' % (90*i)) for i in range(1, 4)],
        'axis': [('h', 'Horizontal'), ('v', 'Vertical')],
    }
    if request.method == 'GET':
        return render_template('submit.html', options=options)
    elif request.method == 'POST':
        text = request.form['text']
        operation = request.form['operation']
        if operation == 'rotate':
             iterations = int(request.form['iterations'])
             clockwise = request.form['clockwise'] == 'negative'
             returned_text = do_rotate(text, iterations, clockwise=clockwise)
        elif operation == 'mirror':
             vertical_axis = request.form['axis'] == 'v'
             returned_text = mirror(text, vertical=vertical_axis)
        elif operation == 'transpose':
             returned_text = transpose(text)
        return render_template('output.html', text=returned_text, operation=operation)

def do_rotate(text, iterations, clockwise=False):
    if clockwise:
        # Subtract from 360 degree rotation in other direction
        iterations = 4 - iterations
    for _ in range(iterations):
        text = rotate(text)
    return text

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
