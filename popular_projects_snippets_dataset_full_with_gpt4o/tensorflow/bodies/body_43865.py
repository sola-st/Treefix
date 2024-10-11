# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_list_test.py
l = []
l.append(1)
l.append(2)
l.append(3)
l.append(4)
ag.set_element_type(l, tf.int32, ())
s = 0
for _ in range(n):
    s += l.pop()
exit((ag.stack(l, strict=False), s))
