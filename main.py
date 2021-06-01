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

@app.route("/avaliation", methods=['GET','POST'])
def avaliation():
    if(request.method == 'GET'):
        global_db = DataBase('podcasts.db')
        avaliation = global_db.getAvaliations()

        res = make_response(jsonify({
            "message": "Success",
            "data": {
                "avaliations": avaliation
            }
        }), 200)
        res.headers['Content-Type'] = "application/json" 
        return res

    if(request.method == 'POST'):
        global_db = DataBase('podcasts.db')
        episode_id = request.json['episode_id']
        rate = request.json['rate']
        print(episode_id, rate)
        avaliation = global_db.createAvaliation(0, episode_id, rate)

        res = make_response(jsonify({
            "message": "Success",
            "data": {
                "avaliation_id": avaliation
            }
        }), 200)
        res.headers['Content-Type'] = "application/json" 
        return res
    
    res = make_response(jsonify({
        "message": "Error! Invalid method"
    }), 400)
    res.headers['Content-Type'] = "application/json" 
    return res


if __name__ == '__main__':
    app.run()


