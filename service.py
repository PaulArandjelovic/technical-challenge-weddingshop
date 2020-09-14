import logging
from lib.__init__ import *


def add_product(product_id, qty):
    """
    Add a an amount of a product to our list
    :param product_id: product id of product to be added
    :param qty: quantity of product to add to our list
    :return: response to return to front end
    """
    try:
        if not qty or not(qty.isdigit()):
            return "BadFormat"
        qty = int(qty)
    except ValueError:
        return "BadFormat"

    logging.info(f'Adding {qty} of item with id -> {product_id} to list')

    cur.execute(f"SELECT * FROM {DB_PRODUCTS} WHERE id = {product_id};")
    stock = cur.fetchone()[4]

    if stock >= qty:
        new_stock = stock - qty
        cur.execute(f"UPDATE {DB_PRODUCTS} SET stock = {new_stock} WHERE id = {product_id};")
    else:
        return "Not enough stock!"

    cur.execute(f"SELECT * FROM {DB_LIST} WHERE id = {product_id};")
    list_prod = cur.fetchone()

    if list_prod is not None:
        stock = list_prod[1]
        new_stock = stock + qty
        cur.execute(f"UPDATE {DB_LIST} SET stock = {new_stock} WHERE id = {product_id};")
    else:
        cur.execute(f"INSERT INTO {DB_LIST} (id, stock) VALUES (%s, %s);", (product_id, qty))

    conn.commit()
    return ""


def remove_product(product_id):
    """
    Remove an item from our list
    :param product_id: product id of product to be removed
    :return: response to return to front end
    """
    logging.info(f'Removing item with id -> {product_id} from list')

    cur.execute(f"SELECT * FROM {DB_LIST} WHERE id = {product_id};")
    list_prod = cur.fetchone()

    if list_prod is not None:
        extra_stock = list_prod[1]
        cur.execute(f"DELETE FROM {DB_LIST} WHERE id = {product_id};")
        cur.execute(f"SELECT * FROM {DB_PRODUCTS} WHERE id = {product_id};")
        product_stock_to_update = cur.fetchone()[4]

        new_stock = extra_stock + product_stock_to_update
        cur.execute(f"UPDATE {DB_PRODUCTS} SET stock = {new_stock} WHERE id = {product_id};")

    conn.commit()
    return ""
