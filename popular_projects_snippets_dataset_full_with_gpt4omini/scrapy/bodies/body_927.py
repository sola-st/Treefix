# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
self.headers = Headers()  # bucket for response headers

# Method command
self.sendCommand(self.factory.method, self.factory.path)
# Headers
for key, values in self.factory.headers.items():
    for value in values:
        self.sendHeader(key, value)
self.endHeaders()
# Body
if self.factory.body is not None:
    self.transport.write(self.factory.body)
