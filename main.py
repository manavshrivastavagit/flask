from flask import Flask, redirect, url_for,request, render_template
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#    return "Hello World"

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


@app.route('/marks/<int:score>')
def marks(score):
   return render_template('marks.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/static')
def stat():
   return render_template("static.html")

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/result1',methods = ['POST', 'GET'])
def result1():
   if request.method == 'POST':
      result = request.form
      return render_template("result1.html",result = result)

@app.route('/')
def index():
   return render_template("login.html",name="mnv")



if __name__ == '__main__':
   app.debug = True
   app.run()