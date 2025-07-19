from flask import Flask

app=Flask(__name__)

@app.get("/")
def Hello():
    return "<h1>Hello from Jenkins CI/CD</h1>"

if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000)