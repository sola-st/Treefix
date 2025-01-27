# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
if lvl is None:
    if self.requests:
        requests = self.requests[max(self.requests)]
    else:
        requests = []
else:
    requests = self.requests.get(lvl, [])

print("# Requests ", "-" * 65)
display.pprint(requests, colorize=colour)
