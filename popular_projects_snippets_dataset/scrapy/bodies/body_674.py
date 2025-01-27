# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
"""Helper function for request_from_dict"""
name = str(name)
try:
    exit(getattr(obj, name))
except AttributeError:
    raise ValueError(f"Method {name!r} not found in: {obj}")
