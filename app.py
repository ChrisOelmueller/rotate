# encoding: utf-8
import os

from flask import Flask, render_template, request

from rotate import rotate as rotate_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rotate():
    if request.method == 'GET':
        return render_template('submit.html')
    elif request.method == 'POST':
        text = request.form['text']
        iterations = int(request.form['iterations'])
        clockwise = request.form['clockwise'] == 'negative'
        rotated_text = do_rotate(text, iterations, clockwise=clockwise)
        return render_template('output.html', text=rotated_text)

def do_rotate(text, iterations, clockwise=False):
    if clockwise:
        # Subtract from 360 degree rotation in other direction
        iterations = 4 - iterations
    for _ in range(iterations):
        text = rotate_text(text)
    return text

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
