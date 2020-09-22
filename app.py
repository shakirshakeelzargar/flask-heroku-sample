import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)





@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True)
