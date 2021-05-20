from flask import Flask, redirect, url_for, request,render_template
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder="./")

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Mysq2021*"
app.config['MYSQL_DB'] = "analysis"
#app.config['MYSQL_CURSORCLASS'] = "upload-folder-path"test
app.config['default_authentication_plugin']="G9NvR4tyGtv1fQhlc8fOmuu4AWCQpwzn"

mysql = MySQL(app)

@app.route("/",methods = ["POST", "GET"])
def main():
   if request.method == "POST":
      _dispositif = request.form["dispositif"];
      _site = request.form["site"]
      _debut= request.form["debut"]
      _fin= request.form["fin"]
      _slct1=request.form["slct1"]
      _slct2=request.form["slct2"]

      _fin1 = request.form["fin1"]
      _fin2 = request.form["fin2"]
      _fin3 = request.form["fin3"]
      _fin4 = request.form["fin4"]
      _fin5 = request.form["fin5"]
      
      _intType= request.form["intType"]  
      _int1 = request.form["int1"]
      _int2 = request.form["int2"]
      _int3 = request.form["int3"]
      _int4 = request.form["int4"]
      _forDis=request.form["forDis"]
      _int5 = request.form["int5"]
      _risqS = request.form["risqS"]
      _risqH = request.form["risqH"]
      _risqJ = request.form["risqJ"]
      _risqEn = request.form["risqEn"]
      _risqEc = request.form["risqEc"]

      _usagers = request.form["usagers"]
      _pres1 = request.form["pres1"]
      _pres2 = request.form["pres2"]
      _pres3 = request.form["pres3"]
      _pres4 = request.form["pres4"]
      _pres5 = request.form["pres5"]
      _pres6 = request.form["pres6"]

      _ben1 = request.form["ben1"]
      _ben2 = request.form["ben2"]
      _ben3 = request.form["ben3"]
      _ben4 = request.form["ben4"]
      _ben5 = request.form["ben5"]
      _ben6 = request.form["ben6"]
      _ben7 = request.form["ben7"]

      _comments = request.form["comments"]
      _feedback = request.form["feedback"]

      print(_dispositif)
      print(_site)
      print(_debut)
      print(_fin)
      print(_slct1)
      print(_slct2)

      print(_fin1)
      print(_fin2)
      print(_fin3)
      print(_fin4)
      print(_fin5)

      print(_intType)
      print(_int1)
      print(_int2)
      print(_int3)
      print(_int4)
      print(_forDis)
      print(_int5)
      print(_risqS)
      print(_risqH)
      print(_risqJ)
      print(_risqEn)
      print(_risqEc)

      print(_usagers)
      print(_pres1)
      print(_pres2)
      print(_pres3)
      print(_pres4)
      print(_pres5)
      print(_pres6)

      print(_ben1)
      print(_ben2)
      print(_ben3)
      print(_ben4)
      print(_ben5)
      print(_ben6)
      print(_ben7)

      print(_comments)
      print(_feedback)

      cur = mysql.connection.cursor()

      cur.execute("INSERT INTO survey(dispositif, site, debut, fin, statue, branche, fin1, fin2, fin3, fin4,fin5,\
          intType, inter1, inter2, inter3, inter4, intForDis, inter5, intRisqS, intRisqH, intRisqJ, intRisqEn, \
          intRisqEc, preUsager, pre1, pre2, pre3, pre4, pre5, pre6, ben1, ben2, ben3, ben4, ben5, ben6, ben7, comment, proposition) \
          VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,\
           %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(_dispositif,_site,_debut,_fin, \
            _slct1, _slct2,_fin1, _fin2, _fin3, _fin4, _fin5, _intType, _int1, _int2, _int3, _int4, _forDis,_int5, \
            _risqS, _risqH, _risqJ, _risqEn, _risqEc,_usagers,_pres1, _pres2, _pres3, _pres4, _pres5, _pres6,_ben1, \
            _ben2, _ben3, _ben4, _ben5, _ben6, _ben7, _comments, _comments));

      mysql.connection.commit()
      cur.close()
   return render_template("index.html")


@app.route("/analysis",methods = ["POST", "GET"])
def analysis():
   return render_template("analysis.html")


if __name__ == '__main__':
   app.run(debug = True)