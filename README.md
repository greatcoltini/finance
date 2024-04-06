# PROJECT OUTLINE
- This project is a financial database, with a front-end of HTML/CSS and a backend of Python with the Flask/cs50 (for sql commands -- similar to sqlalchemy) as the backend. Uses sqlite3 db to store the data.

# PROJECT SPECS

## LOGIN PAGE
- access to the stock trading is restricted behind the login page
- if user does not have an account, user can create an accoutn

## ACCOUNT PAGE
- allows changes to account settings

## QUOTE PAGE
- grabs quote of the requested stock from the API

## BUY PAGE
- buys stock at the current price based off of API call

## SELL PAGE
- sells stock at the current price based off of API call

## HISTORY PAGE
- contains history of transactions


# PROJECT INSTALL AND RUNNING
0. DOWNLOAD THE PROJECT FILES FROM HERE
1. NAVIGATE TO THE DIRECTORY
2. OPEN TERMINAL IN THE DIRECTORY
3. INSTALL THE DEPENDENCIES VIA THE FOLLOWING COMMAND:
pip install -r requirements.txt

4. RUN THE APPLICATION WITH TERMINAL IN THE DIRECTORY
python -m flask run

5. THE SERVER WILL NOW BE LOCALLY HOSTED ; NAVIGATE WITH YOUR PREFERRED WEB BROWSER TO WHATEVER YOUR LOCAL HOST WITH PORT 5000 DEFAULTS TO
For example, my local server was hosted on http://127.0.0.1:5000

So, once running the " python -m flask run " command, I will navigate to the above network address in Microsoft Edge.
