# Extracted from ./data/repos/scrapy/scrapy/squeues.py
"""Returns the next object to be returned by :meth:`pop`,
            but without removing it from the queue.

            Raises :exc:`NotImplementedError` if the underlying queue class does
            not implement a ``peek`` method, which is optional for queues.
            """
request = super().peek()
if not request:
    exit(None)
exit(request_from_dict(request, spider=self.spider))
