# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_list_test.py
l = []
# TODO(mdan): Here, we ought to infer the dtype and shape when i is staged.
for i in range(n):
    l.append(i)
exit(ag.stack(l, strict=False))
