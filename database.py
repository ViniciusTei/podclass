import sqlite3
from rssfeed import FeedRss

class DataBase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def createTable(self):
        #create table
        # self.cursor.execute('''CREATE TABLE podcast
        #               (title, link, summary, image, author, total_episodes)''')
        self.cursor.execute('''CREATE TABLE episodes
                      (title, url, description, thumbnail, members, duration, published_at)''')
    
    def insertRssFeed(self, feed_url):
        # NewsFeed = feedparser.parse("https://anchor.fm/s/fa5d110/podcast/rss")
        # NewsFeed = feedparser.parse("https://desabilitado.com.br/thshow/feed.xml")
        NewsFeed = FeedRss(feed_url)
        # title = NewsFeed.entries
        # print(title)
        # 'authors', 'author', 'author_detail', 'title', 'title_detail', 'summary', 'summary_detail', 'links', 'link', 'published', 'published_parsed', 'itunes_duration', 'tags', 'content', 'subtitle', 'subtitle_detail', 'image', 'itunes_explicit', 'itunes_block'
        self.cursor.execute("insert into podcast values (?, ?, ?, ?, ?, ?)", (NewsFeed.feed.title , NewsFeed.feed.link , NewsFeed.feed.summary , NewsFeed.feed.image.href, NewsFeed.feed.author, len(NewsFeed.entries)))

        feed = []
        for i in range(len(NewsFeed.entries)):
            feed.append((NewsFeed.entries[i].title, NewsFeed.entries[i].link, NewsFeed.entries[i].summary, NewsFeed.entries[i].image.href, NewsFeed.entries[i].author))
        self.cursor.executemany("insert into feed values (?, ?, ?, ?, ?)", feed)
        self.connection.commit()
    
    def selectAllPodcasts(self):
        self.cursor.execute("select * from podcast")
        response = self.cursor.fetchall()
        dictionary = []
        for i in range(len(response)):
                dictionary.append({
                   "title": response[i][0],
                   "link": response[i][1],
                   "summary": response[i][2],
                   "image": response[i][3],
                   "author": response[i][4],
                   "total_episodes": response[i][5],
                })
        
        return dictionary
    
    def selectAllEpisodes(self):
        self.cursor.execute("select * from feed")
        response = self.cursor.fetchall()
        dictionary = []
        for i in range(len(response)):
                dictionary.append({
                   "title": response[i][0],
                   "link": response[i][1],
                   "summary": response[i][2],
                   "image": response[i][3],
                   "author": response[i][4],
                   "total_episodes": response[i][5],
                })
        
        return dictionary