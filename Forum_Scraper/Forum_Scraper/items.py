import scrapy

class ForumScraperItem(scrapy.Item):
    # Holds the post author's name
    author = scrapy.Field()
    # Holds the post author's word count
    wordCount = scrapy.Field()
    # Holds the subject of the post
    postSubject = scrapy.Field()
