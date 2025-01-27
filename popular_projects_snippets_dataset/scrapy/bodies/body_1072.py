# Extracted from ./data/repos/scrapy/scrapy/squeues.py
"""Returns the next object to be returned by :meth:`pop`,
            but without removing it from the queue.

            Raises :exc:`NotImplementedError` if the underlying queue class does
            not implement a ``peek`` method, which is optional for queues.
            """
try:
    s = super().peek()
except AttributeError as ex:
    raise NotImplementedError("The underlying queue class does not implement 'peek'") from ex
if s:
    exit(deserialize(s))
