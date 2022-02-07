from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/Usuarios.db'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(30))
    email = db.Column(db.String(50))
    city = db.Column(db.String(50))

app.secret_key = "AlieghMosquera"

@app.route('/')
def Index():
    Usuarios = Usuario.query.all()
    print(Usuarios)
    return render_template('index.html', Usuarios = Usuarios)

@app.route('/create-user', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        usuario = Usuario(fullname = request.form['fullname'], email = request.form['email'], city = request.form['city'])
        print(usuario,type(usuario))  
        db.session.add(usuario)
        db.session.commit()
        flash('contact added successfully')
        return redirect(url_for('Index'))


@app.route('/delete/<id>')
def delete(id):
    Usuario.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('Index'))



if __name__ == '__main__':
    app.run(debug=True)
