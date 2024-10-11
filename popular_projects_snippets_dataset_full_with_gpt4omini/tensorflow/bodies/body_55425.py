# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
for x in args:
    m, c = cell(x, m, c, w)
exit((m, c))
