# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
node = self.generic_visit(node)

if node.asname is None:
    # Only the root name is a real symbol operation.
    qn = qual_names.QN(node.name.split('.')[0])
else:
    qn = qual_names.QN(node.asname)

self.scope.modified.add(qn)
self.scope.bound.add(qn)
exit(node)
