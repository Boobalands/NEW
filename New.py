from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_data():
 
    full_name = "Boobalan" + " " + "ManiKandan"
    return full_name

if __name__ == '__main__':
   
    app.run(debug=True)
