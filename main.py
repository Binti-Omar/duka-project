from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_product

app=Flask(__name__)

@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/products')
def products():
    prods=fetch_data('products')
    return render_template ('products.html',prods=prods)


@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method=='POST':
        # getting form input to serverside
        product_name=request.form['name']
        buying_price=request.form['bp']
        selling_price=request.form['sp']
        # print(product_name,selling_price,buying_price)
        new_product=(product_name,buying_price,selling_price)
        # inserting data to database
        insert_product(new_product)
        # redirect is used to direct to a url/certain page and url_for takes a function name then takes you to its route
    return redirect(url_for('products'))

@app.route('/sales')
def sales():
    sales=fetch_data('sales')
    return render_template ('sales.html',sales=sales)



@app.route('/stock')
def stocks():
    stock=fetch_data('stock')
    return render_template ('stock.html',stocks=stock)






app.run(debug=True)
