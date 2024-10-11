# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
s = "\t\t\tAGGREGATE %s\n" % self.aggregation
for sort, val in self.names.iteritems():
    s += "\t\t\t%d: %s\n" % (sort, val)
exit(s)
