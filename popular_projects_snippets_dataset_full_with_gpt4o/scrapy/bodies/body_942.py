# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
"""
        Set the status of the request on us.
        @param version: The HTTP version.
        @type version: L{bytes}
        @param status: The HTTP status code, an integer represented as a
        bytestring.
        @type status: L{bytes}
        @param message: The HTTP status message.
        @type message: L{bytes}
        """
self.version, self.status, self.message = version, status, message
