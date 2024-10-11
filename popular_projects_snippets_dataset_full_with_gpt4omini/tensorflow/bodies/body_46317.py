# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_fndefs.py
super(Analyzer, self).__init__(graph)
# This allows communicating that nodes have extra reaching definitions,
# e.g. those that a function closes over.
self.external_defs = external_defs
