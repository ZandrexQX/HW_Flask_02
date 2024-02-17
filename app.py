from flask import Flask, session, render_template, request, redirect, url_for


app = Flask(__name__)
app.secret_key = '87f376591d904e59ea687cd90aac6e19466a7ddeec73e3ca3e7e8e0596a2d56f'


@app.route('/')
@app.route('/index/')
def index():
    if 'username' in session:
        return render_template('main.html', name=session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)