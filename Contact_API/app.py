from flask import Flask,render_template,redirect,request,url_for,jsonify,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')
app.secret_key="qwerty5607"

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///Contactdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    number=db.Column(db.String,nullable=False)
    email=db.Column(db.String(40))
    address=db.Column(db.String(300),default='')
    def __init__(self,name,number,email,address):
        self.name=name
        self.number=number
        self.email=email
        self.address=address
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=='POST':
        nm=request.form["Name"]
        em=request.form["Email"]
        ph=request.form["Number"]
        ad=request.form["Address"]
        add=Contact(name=nm,email=em,number=ph,address=ad)
        try:
            db.session.add(add)
            db.session.commit()
            flash("Contacted Added Successfully")
            return redirect(url_for('add'))
        except:
            flash("There is an error adding your data")
            return redirect(url_for('add'))
    return render_template("add.html")

@app.route("/view",methods=['GET'])
def view():
    if request.method =='GET':
        flash("Viewing All Contact")
        contact=Contact.query.all()
    return render_template('view.html',contact=contact)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)