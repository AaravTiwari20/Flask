from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
            "id":1,
            "title":u"Buy Groceries",
            "description":u"Milk,Cheese,Fruits,Butter,Vegetables",
            "done":False
    },
    {
            "id":2,
            "title":u"Learn Python",
            "description":u"Need To Find A Good Python Tutorial On The Web",
            "done":False
    }
        ]
@app.route("/add-data",methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide The Data"
        },400)
    task = {
            "id":tasks[-1]["id"]+1,
            "title":request.json["title"],
            "description":request.json.get("description",),
            "done":False
    }
    tasks.append(task)
    
    return jsonify({
            "status":"Success",
            "message":"Task Added Successfully"
    })
    
@app.route("/get-data")

def get_task():
    return jsonify({
            "data":tasks
    })
     
def hello_world():
    return  "Hello World"

if __name__ == "__main__":
    app.run(debug = True)
     


