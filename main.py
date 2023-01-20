from flask import Flask, render_template, request
from replit import db

app = Flask('app')

 
@app.route('/')
def index():
  return render_template("index.html")
  
@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.route('/post/new')
def post_new():
  return render_template("post_new.html")

@app.route('/post/create', methods=["POST"])
def post_create():
  db ["posts"].append({
    'title': request.form["title"],
    'content': request.form['content']
    
  })
  return render_template("index.html")


@app.route(  '/team')
def team():
  return render_template("team.html")
 
@app.route('/posts')
def posts():
  return render_template("posts.html", posts=db["posts"])  

@app.route('/posts/<id>')
def show(id):
  return render_template("show.html", post=db["posts"] [int(id)])

@app.route('/eleves')
def eleves():
  return render_template("eleves.html", eleves=db["eleves"])

@app.route('/eleves/<id>')
def showeleves(id):
  return render_template("showeleves.html", eleve=db["eleves"][int(id)])



app.run(host='0.0.0.0', port=8080)
