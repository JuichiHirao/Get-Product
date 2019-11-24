from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return render_template('index.html')


"""
@app.route('/product', methods=['POST'])
def product():
    print('color1 {}'.format(request.form['color1']))
    print('p_number1 {}'.format(request.form['number1']))
    return render_template('result.html')
"""

@app.route('/product', methods=['POST'])
def product():
    print('color1 {}'.format(request.form['color1']))
    print('p_number1 {}'.format(request.form['number1']))
    response = make_response()
    response.data = '{ "abc": 1 }'
    response.headers['Content-Disposition'] = 'attachment; filename=test.json'
    response.mimetype = 'application/json'
    return response

if __name__ == '__main__':
    app.run()
