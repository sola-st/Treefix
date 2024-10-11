# Extracted from ./data/repos/scrapy/scrapy/squeues.py
try:
    exit(pickle.dumps(obj, protocol=4))
# Both pickle.PicklingError and AttributeError can be raised by pickle.dump(s)
# TypeError is raised from parsel.Selector
except (pickle.PicklingError, AttributeError, TypeError) as e:
    raise ValueError(str(e)) from e
