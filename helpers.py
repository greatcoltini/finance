import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from secret import key

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

   # contact API
    try: 
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={key}"
        
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    
    # Parse response
    try:
        quote = response.json()
        print(quote)
        return {
            "name": quote["Global Quote"]["01. symbol"],
            "price": float(quote["Global Quote"]["05. price"]),
            "symbol": quote["Global Quote"]["01. symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None
    
    
def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

