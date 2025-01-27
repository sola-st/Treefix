# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
"""Raises :exc:`Exception` if the installed
    :mod:`~twisted.internet.reactor` does not match the specified import
    path."""
from twisted.internet import reactor
reactor_class = load_object(reactor_path)
if not reactor.__class__ == reactor_class:
    msg = ("The installed reactor "
           f"({reactor.__module__}.{reactor.__class__.__name__}) does not "
           f"match the requested one ({reactor_path})")
    raise Exception(msg)
