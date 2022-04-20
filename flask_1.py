from flask import Flask, render_template

app = Flask(__name__)

menu = ['Adilet', 'Nursultan', 'Bakyt']
# menu = [i for i in range(100, 110)]
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return "<h1>AXAXAXA</h1>"


@app.route('/course')
def loop():
    return render_template('course.html', title='ADILET')


if __name__ == '__main__':
    app.run(debug=True)
