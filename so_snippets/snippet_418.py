# Extracted from https://stackoverflow.com/questions/12836128/convert-list-to-tuple-in-python
l = [4,5,6]
tuple(l)
(4, 5, 6)

tuple = 'whoops'   # Don't do this
tuple(l)
TypeError: 'tuple' object is not callable

