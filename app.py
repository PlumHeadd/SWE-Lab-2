from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def idx():
    return render_template('index.html')

@app.route('/proc', methods=['POST'])
def proc():
    nm = request.form['name']
    ag = request.form['age']
    
    msg = f'Hello {nm}, you are {ag} years old!'
    return render_template('results.html', message=msg)

if __name__ == '__main__':
    app.run(debug=True)