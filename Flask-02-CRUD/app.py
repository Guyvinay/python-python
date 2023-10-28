from flask import Flask , request , render_template, redirect

app = Flask(__name__)

database = {}

@app.route('/create', methods=['POST','GET'])
def create() :
    if request.method == 'POST' :
        key = request.form['key']
        value = request.form['value']
        database[key] = value
        return render_template('create.html')
    return render_template('create.html')

@app.route('/read')
def read() : 
    return render_template('read.html', data = database)

@app.route('/update', methods=['GET','POST'])
def update() :
    if request.method == 'POST' :
        key = request.form['key']
        if key in database :
            value = request.form['value']
            database[key] = value
            return redirect('/read')
        else :
            return 'Key Not Found'
    return render_template('update.html')  

@app.route('/delete', methods=['GET','POST'])
def delete() :
    if request.method == 'POST' :
        key = request.form['key']
        if key in database :
            del database[key]
            return redirect('/read')
        else :
            return 'Key Not Found' 
    return render_template('delete.html')

if __name__ == '__main__' :
    app.run()