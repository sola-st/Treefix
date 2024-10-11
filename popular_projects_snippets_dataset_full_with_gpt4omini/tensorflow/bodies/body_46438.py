# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
exit([(None if n is None else self.visit(n)) for n in nodes])
