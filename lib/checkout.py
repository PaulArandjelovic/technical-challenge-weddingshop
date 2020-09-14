from . import *


def gen_html():
    """
    Generate html for our checkout page
    :return: generated html
    """
    try:
        cur.execute(f"SELECT * FROM {DB_LIST} ORDER BY id ASC;")
        products = cur.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        return ''

    grand_total = 0
    img_src = "static/pics/fork.png"
    items_lst = []

    base_lst = [
        "<div class='cart'>"
            "<ul class='product-list'>"
    ]
    foot_lst = [
           "</ul>"
        "</div>"
    ]

    for row in products:
        p_id, stock = row
        cur.execute(f"SELECT * FROM {DB_PRODUCTS} WHERE id = {p_id};")

        _, name, brand, unit_price, _ = cur.fetchone()
        unit_price = unit_price.split("GBP")[0]
        total_price = "{:.2f}".format(stock * float(unit_price))
        button_class = 'button remove'

        if stock <= 0:
            stock_class = 'item-noStock'
            stock_txt = 'Out of Stock'
        else:
            stock_class = 'item-inStock'
            stock_txt = 'In Stock'

        items_lst.append(
            f"<li id='item_{p_id}'class='cart-item'>"
                "<div class='info-wrap'>"
                    "<div class='item-info'>"
                        f"<img class='item-img' src='{img_src}' alt=''>"
                        f"<p class='item-id'># {p_id}</p>"
                        f"<h3>{name}</h3>"
                        f"<h4>{brand}</h4>"
                        "<p>"
                            f"{stock} x £{unit_price}"
                        "</p>"
                        f"<p class={stock_class}>{stock_txt}</p>"
                    "</div>"

                    "<div class='item-total-price'>"
                        f"<p id='total_price'>£{total_price}</p>"
                    "</div>"

                    "<div class='add-to-cart-wrap'>"
                        f"<button class='{button_class}' onclick='remove_list_item({p_id})' href='#'>Remove</button>"
                    "</div>"
                "</div>"
            "</li>"
        )
        grand_total += stock * float(unit_price)

    grand_total = "{:.2f}".format(grand_total)

    totals_lst = [
        "<div class='subtotal'>"
            "<ul class='total-list'>"
                "<li class='totalRow'>"
                    "<span class='label'>Subtotal</span>"
                    f"<span id='subtotal' class='value'>£{grand_total}</span>"
                "</li>"
                "<li class='totalRow'>"
                    "<span class='label'>Shipping</span>"
                    f"<span class='value'>£0.00</span>"
                "</li>"
                "<li class='totalRow'>"
                    "<span class='label'>Tax</span>"
                    f"<span class='value'>£0.00</span>"
                "</li>"
                "<li class='totalRow final'>"
                    "<span class='label'>Grand Total</span>"
                    f"<span id='grand_total' class='value'>£{grand_total}</span>"
                "</li>"

                # Checkout button
                "<li class='totalRow final'>"
                    "<a class='view-list-button' style='background: #82ca9c;' href='#'>Checkout</a>"
                "</li>"
            "</ul>"
        "</div>"
    ]

    return ''.join(base_lst + items_lst + foot_lst + totals_lst)
