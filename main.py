from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_product,insert_sales,insert_stock,products_profit,sales_product

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
    products=fetch_data('products')
    return render_template ('sales.html',sales=sales,products=products)

@app.route('/add_sale',methods=['GET','POST'])
def add_sale():
    if request.method=='POST':
        productid=request.form['pid']
        quantity=request.form['quantity']
        new_sale=(productid,quantity)
        insert_sales(new_sale)
    return redirect(url_for('sales'))


@app.route('/stock')
def stocks():
    stock=fetch_data('stock')
    products=fetch_data('products')
    return render_template ('stock.html',stocks=stock,products=products)

@app.route('/add_stock',methods=['GET','POST'])
def stock():
    if request.method=='POST':
        pid=request.form['pid']
        stock=request.form['stock quantity']
        new_stock=(pid,stock)
        insert_stock(new_stock)
    return redirect(url_for('stocks'))

@app.route('/dashboard')
def dashboard():
    profit=products_profit()
    sale=sales_product()
    # print(profit)
    # print(sale)
    product_names=[]
    product_profit=[]
    sale_product=[]
    for i in profit:
        product_names.append(i[0])
        product_profit.append(float(i[1]))
        sale_product.append(float(i[1]))
    return render_template('dashboard.html',product_names=product_names,product_profit=product_profit,sale_product=sale_product)


app.run(debug=True)
