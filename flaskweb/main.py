from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/news')
def news():
   return render_template("/news/index_news.html")

@app.route('/news/satu')
def news1():
   return render_template("/news/news1.html")

@app.route('/blog')
def blog():
   return render_template("/blog/index_blog.html")

@app.route('/blog/satu')
def blog1():
   return render_template("/blog/blog1.html")

@app.route('/hitung', methods=['POST', 'GET'])
def hitung():
   hasil = ""
   
   if request.method=="POST":
      hasil = int(request.form['angka'])**3 # PANGKAT TIGA

   return render_template("hitung.html", nilai_akhir=hasil)