from database import DataBase 
from flask import Flask


#db.initDataBase("https://anchor.fm/s/fa5d110/podcast/rss")
app = Flask(__name__)

@app.route("/podcasts", methods=["GET"])
def helloWorld():
    db = DataBase('podcasts.db')
    response = db.selectAllPodcasts()
    return {
        "message": "Success",
        "data": response
    },200

