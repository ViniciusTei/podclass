import sqlite3
import json
import uuid
from models.rssfeed import FeedRss

class DataBase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def createTable(self):
        #create table
        self.cursor.execute('''CREATE TABLE if not exists podcast
                      (id, title, link, authors, language, summary, tags, image_url, total_episodes)''')
        self.cursor.execute('''CREATE TABLE if not exists episode
                      (id, title, members, published, thumbnail, description, file, podcast_id)''')
        self.cursor.execute('''CREATE TABLE if not exists avaliation
                        (id, user_id, episode_id, rate)''')
    
    def insertRssFeed(self, feed_url):
        NewsFeed = FeedRss(feed_url)
        self.createTable()
        self.cursor.execute("insert into podcast values (?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            NewsFeed.podcast['id'], 
            NewsFeed.podcast['title'], 
            NewsFeed.podcast['link'], 
            NewsFeed.podcast['authors'], 
            NewsFeed.podcast['language'], 
            NewsFeed.podcast['summary'], 
            json.dumps(NewsFeed.podcast['tags']),
            NewsFeed.podcast['image_url'],
            NewsFeed.podcast['total_episodes']))

        for i in range(NewsFeed.podcast['total_episodes']):
            self.cursor.execute("insert into episode values (?, ?, ?, ?, ?, ?, ?, ?)", 
               ( NewsFeed.episodes[i]['id'],
                NewsFeed.episodes[i]['title'],
                json.dumps(NewsFeed.episodes[i]['members']),
                NewsFeed.episodes[i]['published'],
                NewsFeed.episodes[i]['thumbnail'],
                NewsFeed.episodes[i]['description'],
                NewsFeed.episodes[i]['file'],
                NewsFeed.episodes[i]['podcast_id']))
        self.connection.commit()
        return NewsFeed.podcast
    
    def selectAllPodcasts(self):
        self.cursor.execute("select * from podcast")
        response = self.cursor.fetchall()
        dictionary = []
        for i in range(len(response)):
            dictionary.append({
                "id": response[i][0],
                "title": response[i][1],
                "link": response[i][2],
                "authors": response[i][3],
                "language": response[i][4],
                "summary": response[i][5],
                "tags": json.loads(response[i][6]),
                "image_url": response[i][7],
                "total_episodes": response[i][8],
            })
        
        return dictionary
    
    def selectAllEpisodes(self, limit, offset):
        self.cursor.execute("select * from episode limit ? offset ?", (limit, offset))
        response = self.cursor.fetchall()
        dictionary = []
        
        for i in range(len(response)):
            
            dictionary.append({
                "id": response[i][0],
                "title": response[i][1],
                "members": json.loads(response[i][2]),
                "published": response[i][3],
                "thumbnail": response[i][4],
                "description": response[i][5],
                "file": response[i][6],
            })
        
        self.cursor.execute("select * from avaliation limit ? offset ?", (limit, offset))
        response = self.cursor.fetchall()
        for i in range(len(dictionary)):
            for j in range(len(response)):
                if(dictionary.id == response[j][2]):
                    dictionary[i].avaliation = response[j][3]
                else:
                    dictionary[i].avaliation = 0
        return dictionary
    
    def selectEpisodeById(self, id):
        self.cursor.execute("SELECT * FROM episode WHERE id=?", (id,))
        response = self.cursor.fetchall()
        dictionary = []
        
        for i in range(len(response)):
            
            dictionary.append({
                "id": response[i][0],
                "title": response[i][1],
                "members": json.loads(response[i][2]),
                "published": response[i][3],
                "thumbnail": response[i][4],
                "description": response[i][5],
                "file": response[i][6],
            })
        
        return dictionary
    
    def createAvaliation(self, user_id, episode_id, rate):
        self.createTable()
        self.cursor.execute("select * from avaliation where episode_id=?", (episode_id,))
        avaliations = self.cursor.fetchall()
        if(avaliations):
            avaliation_id = avaliations[0][0]
            self.cursor.execute("update avaliation set rate=? where episode_id=?", (rate, episode_id,))
            self.connection.commit()

        else:    
            avaliation_id = uuid.uuid4().hex
            self.cursor.execute("insert into avaliation values (?, ?, ?, ?)", (
                avaliation_id,
                user_id,
                episode_id,
                rate
                ))
            self.connection.commit()
        return avaliation_id

    def getAvaliations(self):
        self.cursor.execute("select * from avaliation ")
        return self.cursor.fetchall()