from flask import Flask, render_template

app = Flask(__name__)


@app.route('/sign-in')
def sign_in():  # put application's code here
    return render_template('sign-in.html')

@app.route('/homepage')
def home_page():  # put application's code here
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run()


