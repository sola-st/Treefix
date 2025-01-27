# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
"""Assert the scope contains specific used, modified & created variables."""
self.assertSymbolSetsAre(used, scope.read, 'read')
self.assertSymbolSetsAre(modified, scope.modified, 'modified')
