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
    search=request.args.get("search")
    if search:
        contact= Contact.query.filter(Contact.name.contains(search)|Contact.email.contains(search)).order_by(Contact.name).all()
    elif request.method =='GET':
        flash("Viewing All Contact")
        contact=Contact.query.order_by(Contact.name).all()
    return render_template('view.html',contact=contact)

@app.route("/manage",methods=["GET"])
def manage():
    search=request.args.get("search")
    if search:
        contact= Contact.query.filter(Contact.name.contains(search)|Contact.email.contains(search)).order_by(Contact.name).all()
    elif request.method =='GET':
        contact=Contact.query.order_by(Contact.name).all()
        return render_template("manage.html",contact=contact)
    return render_template("manage.html") 

@app.route("/delete/<int:id>",methods=["GET","DELETE"])
def todelete(id):
    Dcontact=Contact.query.get_or_404(id)
    try:
        db.session.delete(Dcontact)
        db.session.commit()
        flash("The Task Has been Deleted")
        if request.method=="DELETE":    
            return jsonify({"Success":True})
        return redirect(url_for('manage'))
    except:
        if request.method=="DELETE":
            return jsonify({"Success":False}),500
        return "There was a prob deleting that task"

@app.route("/update/<int:id>",methods=["GET","POST"])
def toupdate(id):
    contact=Contact.query.get_or_404(id)
    if request.method=="POST":    
        contact.name=request.form['Name']
        contact.email=request.form['Email']
        contact.number=request.form['Number']
        contact.address=request.form['Address']
        try:
            db.session.commit()
            flash("Contact updated Successfully")
            return redirect (url_for('manage'))
        except:
            flash("Error Occured While Updating Your Contact")
            return redirect(url_for('toupdate',id=contact.id))
    return render_template("update.html",contact=contact)



if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)