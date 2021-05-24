import feedparser

class FeedRss:
    def __init__(self, url):
        self.feed = feedparser.parse(url)