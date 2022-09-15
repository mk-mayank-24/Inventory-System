from asyncio import QueueEmpty
import sqlite3
from unicodedata import name
# from urllib import request
from flask import Flask, render_template, request, url_for ,redirect
app = Flask(__name__)
con = sqlite3.connect("Database.db" , check_same_thread=False)
cur = con.cursor()

@app.route('/')
def product():
    cur.execute("Select * from product" )
    proAvl=cur.fetchall()
    # print(proAvl)
    return render_template("product.html" , productAvilable = proAvl )

@app.route('/location')
def location():
    
    loc=cur.execute("SELECT * FROM location" ).fetchall()
    return render_template("location.html" , location = loc)

@app.route('/productMovement')
def productMovement():
    pm=cur.execute("SELECT productmovement.id,product.id,product.name,location.id,location.location,qty FROM product,location,productmovement where productmovement.pid = product.id and productmovement.warehouse = location.id" ).fetchall()
    print(pm)
    return render_template("productMovement.html" , pm = pm)

@app.route('/addProduct')
def addProduct():
    return render_template("addproduct.html")

@app.route('/updateProduct/<int:id>', methods=['GET', 'POST'])
def updateProduct(id):
    # cur.execute("Select * from product where id = ?" ,(id))
    proAvl= cur.execute("Select * from product where id = ?" ,(id,)).fetchall()
    # print(proAvl[0])
    return render_template("updateProduct.html" , pro = proAvl[0])

@app.route('/addLocation')
def addlocation():
    return render_template("addLocation.html")

@app.route('/updateLocation/<int:id>' , methods=['GET' , 'POST'])
def updatelocation(id):
    loc= cur.execute("Select * from location where id = ?" ,(id,)).fetchall()
    print(loc)
    return render_template("updateLocation.html" , loc=loc[0])


@app.route('/addProductMovement')
def addproductMovement():
    pro=cur.execute("SELECT id,name FROM product" ).fetchall()
    loc=cur.execute("SELECT * FROM location" ).fetchall()
    return render_template("addProductMovement.html" , product = pro , location = loc)


@app.route('/updateProductMovement/<int:id>', methods=['GET', 'POST'])
def updateproductMovement(id):
    pm=cur.execute("SELECT productmovement.id,product.id,product.name,qty FROM product,productmovement where productmovement.pid = product.id and productmovement.id =?" ,(id,) ).fetchall()
    loc=cur.execute("SELECT * FROM location" ).fetchall()
    print(pm)
    print(loc)
    return render_template("updateProductMovement.html" , pm=pm[0] , loc = loc)

@app.route('/addProductDB' ,methods=[ 'GET', 'POST'])
def addProduct1():
    if request.method == 'POST':
        name = request.form['name']
        price = int(request.form['price'])
        desc = request.form['description']
        cur.execute("INSERT INTO product (name,price,Description) VALUES (?,?,?)",(name,price,desc) )
        con.commit()
    return redirect(url_for('product'))

@app.route('/updateProductDB' ,methods=[ 'GET', 'POST'])
def updateProduct1():
    print(request.form['Name'])
    if request.method == 'POST':
        id = int(request.form['id'])
        name = request.form['Name']
        price = int(request.form['Price'])
        desc = request.form['Description']

        cur.execute("UPDATE product SET name = ? , price = ? , Description =? WHERE id = ?",(name,price,desc,id) )
        con.commit()
    return redirect(url_for('product'))
    
@app.route('/deleteProductDB/<int:id>' ,methods=[ 'GET', 'POST'])
def deleteProduct1(id):
    
    cur.execute("DELETE from product  WHERE id = ?",(id,) )
    con.commit()
    return redirect(url_for('product'))

@app.route('/addLocationDB' ,methods=[ 'GET', 'POST'])
def addLocation1():

    if request.method == 'POST':
        loc = request.form['loc']
        cur.execute("INSERT INTO location(location) VALUES(?)",(loc,) )
        con.commit()
    return redirect(url_for('location'))

@app.route('/updateLocationDB' ,methods=[ 'GET', 'POST'])
def updatelocation1():

    if request.method == 'POST':
        print("asa")
        id = int(request.form['id'])
        loc = request.form['loc']

        cur.execute("UPDATE location SET location = ? WHERE id = ?",(loc,id) )
        con.commit()
    return redirect(url_for('location'))

@app.route('/deleteLocationDB/<int:id>' ,methods=[ 'GET', 'POST'])
def deletelocation1(id):

    cur.execute("DELETE from location  WHERE id = ?",(id,) )
    con.commit()
    return redirect(url_for('location'))

@app.route('/addProductMovementDB',methods=[ 'GET', 'POST'])
def addproductMovement1():
    if request.method == 'POST':
        pid = request.form['products']
        warehouse = int(request.form['location'])
        qty = request.form['qty']
        cur.execute("INSERT INTO productmovement (pid,warehouse,qty) VALUES (?,?,?)",(pid,warehouse,qty) )
        con.commit()
    return redirect(url_for('productMovement'))

@app.route('/updateProductMovementDB' ,methods=[ 'GET', 'POST'])
def updateProductmovement1():

    if request.method == 'POST':
        id = int(request.form['id'])
        loc = int(request.form['location'])
        Qty = request.form['qty']

        cur.execute("UPDATE productmovement SET warehouse = ? ,qty = ? WHERE id = ?",(loc,Qty,id) )
        con.commit()
    return redirect(url_for('productMovement'))

@app.route('/deleteProductMovementDB/<int:id>' ,methods=[ 'GET', 'POST'])
def deleteProductMovement1(id):

    cur.execute("DELETE from productmovement  WHERE id = ?",(id,) )
    con.commit()
    return redirect(url_for('productMovement'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)