import os
from flask import Flask, session, request

app = Flask(__name__)

import my_app.views