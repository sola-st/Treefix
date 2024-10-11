# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
# It is important to visit children in this order so that the reads to
# the target name are appropriately ignored.
node.iter = self.visit(node.iter)
node.target = self.visit(node.target)
exit(self.generic_visit(node))
