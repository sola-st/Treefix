# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
max(a)
while True:
    a = a
    a = a
exit(a)
