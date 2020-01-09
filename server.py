#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import json
import sys
import os
from flask import Flask, request, render_template
from subscriber import Subscriber

parser = argparse.ArgumentParser()

parser.add_argument(
    "--host", default="0.0.0.0", help="The host of the server(eg. 0.0.0.0)")
parser.add_argument(
    "--port", default=8500, help="The port of the server(eg. 8500)", type=int)
parser.add_argument(
    "--debug",
    default=True,
    help="Enable debug for flask or not(eg. False)",
    type=bool)

args = parser.parse_args(sys.argv[1:])
application = Flask(__name__)

@application.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@application.route("/subscribe", methods=["POST"])
def subscriber():
    URL = request.form['url']
    email = request.form['email']
    product = Subscriber(URL,email)
    product.subscribe()
    message = "Thanks for subscribing for updates on product on email-ID "+ email
    return render_template('thanks.html',message=message,url=URL)

def main():
    port = int(os.environ.get('PORT', args.port))
    application.run(host=args.host, port=port, debug=args.debug)
	
if __name__ == "__main__":
	main()
