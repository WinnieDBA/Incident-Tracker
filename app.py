from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Trump2019'
app.config['MYSQL_DB'] = 'incident_tracker'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template('welcome.html')


@app.route("/register",methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        platform = request.form['platform']
        incident = request.form['incident']
        source = request.form['source']
        mno = request.form['mno']
        byWho = request.form['raised_by']

        print(platform)
        print(incident)
        print(source)
        print(mno)
        print(byWho)

        cursor = mysql.connection.cursor()
        stm = '''INSERT INTO incident (Platform,Features,Source, mno, raiser) VALUES (%s,%s,%s,%s,%s)'''

        cursor.execute(stm,(platform,incident,source,mno,byWho))
        mysql.connection.commit()
        cursor.close()
        #cursor.commit()

        return render_template('register.html')

       
        
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)