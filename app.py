import os 
from flask import Flask 
from flask import render_template , request, redirect
from flask import send_from_directory




        



app=Flask(__name__)


@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/menú')
def menú():
    return render_template('sitio/menú.html')

@app.route("/css/<archivocss>")
def css_link(archivocss):
    return send_from_directory(os.path.join('templates/sitio/css'),archivocss)


@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/nuestras sedes')
def nuestrassedes():
    return render_template('sitio/nuestras sedes.html')

@app.route('/admin/')
def admin():
    return render_template('admin/index.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/menú')
def admin_menú(): 

    return render_template('admin/menú.html')



@app.route('/admin/menú/guardar', methods=['post'])
def admin_menú_guardar():
    _nombre=request.form['txtNombre']
    _url=request.form['txtURL']
    _archivo=request.files['txtImagen']

   

    

    


    print(_nombre)
    print(_url)
    print(_archivo)

    return redirect('/admin/menú')
   


















if __name__=='__main__':
    app.run(debug=True)

    











