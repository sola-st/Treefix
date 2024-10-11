# Extracted from https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
import itertools
for item in itertools.chain(listone, listtwo):
    # Do something with each list item

