from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('hello.html', name=request.args.get('name'))

@app.errorhandler(404)
def handle_404(error):
    return render_template('error.html', error_message=str(error), status_code=404)


if __name__ == '__main__':
    app.run(host='0.0.0.0')