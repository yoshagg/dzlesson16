from . import models
from flask import current_app as app

@app.route('/')
def foo():
    return 'ass we can'
