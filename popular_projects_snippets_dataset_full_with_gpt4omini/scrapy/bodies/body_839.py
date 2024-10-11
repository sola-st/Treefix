# Extracted from ./data/repos/scrapy/scrapy/core/http2/agent.py
"""Close all the HTTP/2 connections and remove them from pool

        Returns:
            Deferred that fires when all connections have been closed
        """
for conn in self._connections.values():
    conn.transport.abortConnection()
