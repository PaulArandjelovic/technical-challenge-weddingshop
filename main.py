#!/usr/bin/python

import os
from lib import products_home, checkout
from flask import Flask, render_template, send_from_directory, request
from service import add_product, remove_product

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/product_list")
def product_list():
    return render_template("checkout.html")


@app.route("/request_manager/<string:cmd>", methods=['GET'])
def request_manager(cmd):
    resp = ''

    if cmd == 'gen_prod_table':
        resp = products_home.gen_html()
    elif cmd == 'gen_checkout_table':
        resp = checkout.gen_html()
    elif cmd == 'add_list_item':
        resp = add_product(
            product_id=request.args.get('p_id'),
            qty=request.args.get('qty')
        )
    elif cmd == 'remove_list_item':
        resp = remove_product(product_id=request.args.get('p_id'))

    return resp


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        directory=os.path.join(app.root_path, 'static/pics'),
        filename='favicon.png',
        mimetype='image/vnd.microsoft.icon'
    )


if __name__ == "__main__":
    app.run()
