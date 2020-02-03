from flask import Flask
from flask import jsonify
import wikipedia

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return '<h1>Hello, this is a mini Wikipeida.</h1> <br> Please enter the company you want to search on Wikipedia in the format of the following url:<br> <br> https://gcpminiwiki.appspot.com/wikipedia/company_name<br>'

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """
@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    result = wikipedia.summary(company, sentences=100)
    url = wikipedia.page(company).url
    return "<b>Company name</b> <br>{}<br> <br> <b>Summary</b> <br> {} <br> <br> <b>link: </b> <br> {}".format(company, result, url)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)