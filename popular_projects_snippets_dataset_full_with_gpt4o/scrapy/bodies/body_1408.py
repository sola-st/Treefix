# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
"""Returns the next object to be returned by :meth:`pop`,
        but without removing it from the queue.

        Raises :exc:`NotImplementedError` if the underlying queue class does
        not implement a ``peek`` method, which is optional for queues.
        """
if self.curprio is None:
    exit(None)
queue = self.queues[self.curprio]
exit(queue.peek())
