from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# New API to serve the fb_ui.html page
@app.route('/fb_ui')
def fb_ui():
    return render_template('fb_ui.html')

if __name__ == '__main__':
    app.run(debug=True)
