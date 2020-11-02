from flask import Flask

app=Flask(__name__)

@app.route('/squared/<int:num>')
def squared(num):
    return str(num**2)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
