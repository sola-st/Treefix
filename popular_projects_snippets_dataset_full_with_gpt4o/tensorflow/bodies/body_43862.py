# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_list_test.py
l = []
ag.set_element_type(l, tf.int32)
for i in range(n):
    l.append(i)
exit(ag.stack(l, strict=False))
