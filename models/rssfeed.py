import feedparser
import uuid

class FeedRss:
    def __init__(self, url):
        response = feedparser.parse(url)
        self.podcast = {
            "id": uuid.uuid4().hex,
            "title": response.feed.title,
            "link": response.feed.link,
            "authors": response.feed.author,
            "language": response.feed.language,
            "summary": response.feed.summary,
            "tags": response.feed.tags,
            "image_url": response.feed.image.href,
            "total_episodes": len(response.entries)
        }
        episodes_list = []
        
        for i in range(len(response.entries)):
            episodes_list.append({
                "id": uuid.uuid4().hex,
                "title": response.entries[i].title,
                "members": response.entries[i].authors,
                "published": response.entries[i].published,
                "thumbnail": response.entries[i].image.href,
                "description": response.entries[i].summary,
                "file": response.entries[i].links[1].href,
                "podcast_id": self.podcast['id']
            })
        
        self.episodes = episodes_list
           
        