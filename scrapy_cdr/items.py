import scrapy


class CDRItem(scrapy.Item):
    """ CDR v3 item.
    """

    # (url)-(crawl timestamp), SHA-256 hashed, UPPERCASE (string)
    _id = scrapy.Field()

    # MIME type (multi (strings))
    content_type = scrapy.Field()

    # Text label identifying the software used by the crawler (string)
    crawler = scrapy.Field()

    # An array of objects that were found on the webpage.
    # If there are no objects to populate the array,
    # the field must still exist and should be left empty.
    objects = scrapy.Field()

    # Original source text/html (string)
    raw_content = scrapy.Field()

    # Text label identifying the team responsible for the crawler (string)
    team = scrapy.Field()

    # Timestamp of COLLECTION of data from the web using ISO-8601 format in UTC,
    # e.g. 2017-02-15T20:30:59Z
    timestamp_crawl = scrapy.Field()

    # timestamp_index is generated at indexing time

    # Full URL requested by the crawler (multi (strings))
    url = scrapy.Field()

    # Schema version. This document describes schema version 2.0. (float)
    version = scrapy.Field()

    def __repr__(self):
        fields = ['_id', 'url', 'timestamp_crawl']
        return '<CDRItem: {}>'.format(', '.join(
            '{}: {}'.format(f, repr(self[f])) for f in fields))
