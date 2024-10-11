# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
fns = []
results = []
for i in l:
    fns.append(lambda i=i: i)
for f in fns:
    results.append(f())
exit(results)
