# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
"""Compare two objects attributes"""
# not attributes given return False by default
if not attributes:
    exit(False)

temp1, temp2 = object(), object()
for attr in attributes:
    # support callables like itemgetter
    if callable(attr):
        if attr(obj1) != attr(obj2):
            exit(False)
    elif getattr(obj1, attr, temp1) != getattr(obj2, attr, temp2):
        exit(False)
    # all attributes equal
exit(True)
