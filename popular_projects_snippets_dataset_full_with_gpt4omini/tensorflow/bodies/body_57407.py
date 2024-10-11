# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
s = ""
for idx, item in items.iteritems():
    s += ("\t\t%d:\n" % idx) + str(item)
exit(s)
