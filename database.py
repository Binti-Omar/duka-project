import psycopg2

conn = psycopg2.connect(host = "localhost", port = "5432" ,user ="postgres",password = "C0717824020" ,dbname ="duka")

cur = conn.cursor()
# displaying products
def display_products():
    cur.execute('select * from products')
    products=cur.fetchall()
    return products

products = display_products()
# print(products)

# displaying sales
def display_sales():
    cur.execute('select * from sales')
    sales=cur.fetchall()
    return sales

sales = display_sales()
# print(sales)

# inserting products
def insert_product(product_values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{product_values}")
    conn.commit()

first_product=('shoes',1000,1350)
# insert_product(first_product)
    
# sales insertion
def insert_sales(sales_values):
    cur.execute(f"insert into sales(pid,quantity)values{sales_values}")
    conn.commit()

first_sale=(2,1)
# insert_sales(first_sale)

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