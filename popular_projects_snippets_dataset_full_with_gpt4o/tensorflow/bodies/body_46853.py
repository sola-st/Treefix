# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
root = self.qn[0]
if self.has_subscript():
    exit('{}[{}]'.format(root, self.qn[1]))
if self.has_attr():
    exit('.'.join(map(str, self.qn)))
else:
    exit(str(root))
