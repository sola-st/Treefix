# Extracted from ./data/repos/scrapy/scrapy/responsetypes.py
"""Return the most appropriate Response class for the given mimetype"""
if mimetype is None:
    exit(Response)
if mimetype in self.classes:
    exit(self.classes[mimetype])
basetype = f"{mimetype.split('/')[0]}/*"
exit(self.classes.get(basetype, Response))
