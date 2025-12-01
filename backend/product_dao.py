from sql_connection import get_sql_connection
 
def get_all_products(connection):


    
    cur = connection.cursor()

    #inner join means rows with are matching on both tables
    query="select product.product_id,product.name,product.uom_id,product.price_of_each,uom.uom_name from product inner join uom on product.uom_id=uom.uom_id;"

    cur.execute(query)
    rows = cur.fetchall()
    response =[]
    for (product_id,name,uom_id,price_of_each,uom_name) in rows:
        response.append(
            {
                'product_id':product_id,
                'name':name,
                'uom_id':uom_id,
                'price_of_each':price_of_each,
                'uom_name':uom_name
                
            }
        )
        # print(product_id,name,uom_id,price_of_each,uom_name)
    
    
    return response

def insert_new_product(connection,product):
    cursor = connection.cursor()
    query =("insert into product(name,uom_id,price_of_each) values (%s, %s,%s);")
    
    data = (product['product_name'],product['uom_id'],product['price_of_each'])
    cursor.execute(query,data)
    connection.commit()
    
    return cursor.lastrowid

def delete_product(connection,product_id):
    cursor = connection.cursor()
    query =("delete from product where product_id=" +str(product_id))
    
    cursor.execute(query)
    connection.commit()


if __name__ =="__main__":
    connection = get_sql_connection()
    print(delete_product(connection,14))
    print(get_all_products(connection))
