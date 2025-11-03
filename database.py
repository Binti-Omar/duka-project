import psycopg2

conn = psycopg2.connect(host = "localhost", port = "5432" ,user ="postgres",password = "C0717824020" ,dbname ="duka")

cur = conn.cursor()
# displaying products
def fetch_products():
    cur.execute('select * from products')
    prods=cur.fetchall()
    return prods

products = fetch_products()
# print(products)

# displaying sales
def fetch_sales():
    cur.execute('select * from sales')
    sales=cur.fetchall()
    return sales

sales = fetch_sales()
# print(sales)

# displaying stock
def fetch_stock():
    cur.execute('select * from stock;')
    stock = cur.fetchall()
    return stock

stock1 = fetch_stock()
# print(stock1)

# fetch data in the database 
def fetch_data(table):
    query = f'select * from {table}'
    cur.execute(query)
    data=cur.fetchall()
    return data


products=fetch_data('products')
# print(products)
stock=fetch_data('stock')
# print(stock)
sales=fetch_data('sales')
# print(sales)

# inserting products
def insert_product(product_values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{product_values}")
    conn.commit()

first_product=('Roses',100,250)
second_product=('Daises',300,500)
third_product=('Teddy bear',1000,1350)
fourth_product=('Gift vouchers',4000,5000)
fifth_product=('Ladies gift set',2999,3500)
sixth_product=('Blue notebook',500,900)
seventh_product=('Customized trophy award',2999,3500)

# insert_product(first_product)
# insert_product(second_product)
# insert_product(third_product)
# insert_product(fourth_product)
# insert_product(fifth_product)
# insert_product(sixth_product)
# insert_product(seventh_product)



# sales insertion
def insert_sales(sales_values):
    cur.execute(f"insert into sales(pid,quantity)values{sales_values}")
    conn.commit()

first_sale=(2,1)
second_sale=(5,2)
third_sale=(4,4)
fourth_sale=(1,3)
fifth_sale=(3,5)
sixth_sale=(7,30)
# insert_sales(first_sale)
# insert_sales(second_sale)
# insert_sales(third_sale)
# insert_sales(fourth_sale)
# insert_sales(fifth_sale)
# insert_sales(sixth_sale)


# stock insertion
def insert_stock(stock_values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{stock_values}")
    conn.commit()

first_stock=(4,100)
second_stock=(1,59)
third_stock=(5,440)
fourth_stock=(3,30)
fifth_stock=(2,509)
# insert_stock(first_stock)
# insert_stock(second_stock)
# insert_stock(third_stock)
# insert_stock(fourth_stock)
# insert_stock(fifth_stock)



# displaying profits per products
def products_profit():
    query='select products.name as p_name, sum((products.selling_price -products.buying_price)* sales.quantity) as profit from products inner join sales on products.id = sales.pid group by products.id ;'
    cur.execute(query)
    profit=cur.fetchall()
    return profit

myprofits=products_profit()
# print(f'my products profits is { myprofits}')

# displaying sales per product
def sales_product():
    query='select products.name as p_name , sum(products.selling_price * sales.quantity) as total_sales from sales inner join products on products.id = sales.pid group by p_name ;'
    cur.execute(query)
    sales=cur.fetchall()
    return sales
mysales=sales_product()
# print(f'my sales per product are {mysales}')



