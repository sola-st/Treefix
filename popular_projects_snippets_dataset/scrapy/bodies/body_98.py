# Extracted from ./data/repos/scrapy/scrapy/spiders/feed.py
"""Receives a response and a dict (representing each row) with a key for
        each provided (or detected) header of the CSV file.  This spider also
        gives the opportunity to override adapt_response and
        process_results methods for pre and post-processing purposes.
        """

for row in csviter(response, self.delimiter, self.headers, quotechar=self.quotechar):
    ret = iterate_spider_output(self.parse_row(response, row))
    for result_item in self.process_results(response, ret):
        exit(result_item)
