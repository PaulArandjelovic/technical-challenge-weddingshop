from . import *


def gen_html():
    """
    Generate html for our products page
    :return: generated html
    """
    try:
        cur.execute(f"SELECT * FROM {DB_PRODUCTS} ORDER BY id ASC;")
        products = cur.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        return ''

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
        p_id, name, brand, price, stock = row

        if stock <= 0:
            stock_class = 'item-noStock'
            stock_txt = 'Out of Stock'
            button_class = 'button disabled'
            onclick = ''
        else:
            stock_class = 'item-inStock'
            stock_txt = 'In Stock'
            button_class = 'button'
            onclick = f'add_to_list({p_id})'

        items_lst.append(
            "<li class='cart-item'>"
                "<div class='info-wrap'>"
                    "<div class='item-info'>"
                        f"<img class='item-img' src='{img_src}' alt=''>"
                        f"<p class='item-id'># {p_id}</p>"
                        f"<h3>{name}</h3>"
                        f"<h4>{brand}</h4>"
                        "<p>"
                            "<label>"
                                f"<input id='{p_id}_input'class='item-qty' type='text' placeholder='0'>"
                            "<label>"
                            f"x £{price.split('GBP')[0]}"
                        "</p>"
                        f"<p class={stock_class}>{stock_txt}</p>"
                    "</div>"

                    "<div class='item-total-price'>"
                        "<p>£0.00</p>"
                    "</div>"
    
                    "<div class='add-to-cart-wrap'>"
                        f"<button class='{button_class}' onclick='{onclick}' href='#'>Add to list</button>"
                    "</div>"
                "</div>"
            "</li>"
        )

    return ''.join(base_lst + items_lst + foot_lst)
