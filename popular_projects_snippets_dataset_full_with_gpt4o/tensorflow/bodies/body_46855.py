# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
"""Simple symbol form."""
ssfs = [n.ssf() if isinstance(n, QN) else n for n in self.qn]
ssf_string = ''
for i in range(0, len(self.qn) - 1):
    if self.has_subscript():
        delimiter = '_sub_'
    else:
        delimiter = '_'
    ssf_string += ssfs[i] + delimiter
exit(ssf_string + ssfs[-1])
