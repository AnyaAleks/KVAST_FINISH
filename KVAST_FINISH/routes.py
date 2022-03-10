"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/thingworx')
@view('thingworx')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/blockchain')
@view('blockchain')
def about():
    """Renders the about page."""
    return dict(
        title='Blockchain',
        message='Your application description page.',
        year=datetime.now().year
    )
