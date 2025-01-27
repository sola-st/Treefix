# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
"""Hash key for Python dict."""
# Python dict is unhashable. Creates a sorted dict and dumps as json str.
d = collections.OrderedDict(sorted(loc.items(), key=lambda x: x[0]))
exit(json.dumps(d))
