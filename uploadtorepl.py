from flask import Flask, request, render_template,jsonify
 
app = Flask(__name__, template_folder='template')
  
@app.route('/', methods = ['GET', 'POST'])
def Index():
  return "this is a webside"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
 
@app.route('/getcmd', methods = ['GET', 'POST'])
def getcmd():
    f = open("test.txt", "r")
    
  
    return f.read()

client = app.test_client()
@app.route('/<string:name>/')
def incrementer(name):
    f = open("test.txt", "w")
    f.write(name)
    f.close()
    print(name)
    return "finished"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8000)
