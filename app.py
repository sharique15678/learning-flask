from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    userEmail = "sharique@email.com"
    userPassword = "password"
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == "POST":
        data = request.form
        email = data.get('email')
        password = data.get('password')
        if email==userEmail and password==userPassword:
            return "welcome"
        else:
            return redirect('/login')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == "POST":
        data = request.form
        print(data.get('name1'))
        print(data.get('email'))
        print(data.get('phone'))
        print(data.get('password'))
        return "register success"


if __name__ =="__main__":
    app.run(debug=True)