from flask import Flask,request,render_template
from datetime import datetime

bonjour = Flask(__name__)

@bonjour.route('/')
@bonjour.route('/index')
def index():
	return render_template("patron.html")

@bonjour.route("/table")
def table():
	return render_template("table.html")

@bonjour.route("/looptemplate")
def looptpl():
	listeNoms = ['AFX','Squarepusher','Plaid','Faith No More','Thundercat']
	listeGenres = ['Electronica','Drill and Bass','IDM','Alt Metal','Afrofuturism']
	return render_template("patron-loop.html",len=len(listeNoms),nom=listeNoms,genre=listeGenres)

@bonjour.route('/date')
def afficherDate():
        d = datetime.now()
        sdate = d.strftime("%Y-%m-%d")
        return render_template("date.html", ladate=sdate)

@bonjour.route('/form_get')
def fget():
	return render_template("patron-get.html")

@bonjour.route("/form_get_reponse")
def bonjget():
        nom = request.args.get('n')
        prenom = request.args.get('p')
        return render_template("patron-get-reponse.html", leprenom = prenom, lenom = nom)

@bonjour.route('/form_post')
def fpost():
	return render_template("patron-post.html")

@bonjour.route('/form_post_reponse', methods=['POST'])
def fpostrep():
        nom = request.form['n']
        prenom = request.form['p']
        return render_template('patron-get-reponse.html', leprenom=prenom, lenom=nom)
