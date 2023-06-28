from flask import Flask

app = Flask(__name__)

# create a home route
@app.route('/')
def home():
  return "<h1> This is the Homepage</h1>"

if __name__ =='__main__':
  app.run(host='0.0.0.0', debug= True)