from controllers.database import DataBase 
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

def getPodcasts():
    db = DataBase('podcasts.db')
    response = db.selectAllPodcasts()
    res = make_response(jsonify({
        "message": "Success",
        "data": response
    }), 200)
    res.headers['Content-Type'] = "application/json"
    return res

def postPodcast():
    db = DataBase('podcasts.db')
    response = db.insertRssFeed(request.json['url'])
    res = make_response(jsonify({
        "message": "Success",
        "data": response
    }), 200)
    res.headers['Content-Type'] = "application/json"
    return res

@app.route("/podcasts", methods=['GET', 'POST'])
def podcast():
    if(request.json):
        return postPodcast()
    else:
       return getPodcasts() 


@app.route("/episodes/<string:id>", methods=['GET'])
def episodeById(id):
    
    db = DataBase('podcasts.db')
    response = db.selectEpisodeById(id)
    
    res = make_response(jsonify({
        "message": "Success",
        "data": response
    }), 200)
    res.headers['Content-Type'] = "application/json"
    return res

@app.route("/episodes", methods=['GET'])
def episodes():
    limit = request.args.get('limit', default = 20, type = int)
    offset = request.args.get('offset', default = 1, type = int)

    db = DataBase('podcasts.db')
    response = db.selectAllEpisodes(limit, offset)
    
    res = make_response(jsonify({
        "message": "Success",
        "data": response
    }), 200)
    res.headers['Content-Type'] = "application/json"
    return res


if __name__ == '__main__':
    app.run()


