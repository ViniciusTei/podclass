from database import DataBase 

db = DataBase('podcasts.db')
db.initDataBase("https://anchor.fm/s/fa5d110/podcast/rss")
db.select()
