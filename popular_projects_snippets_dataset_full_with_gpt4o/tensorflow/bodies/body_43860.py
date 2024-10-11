# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_list_test.py
l = []
l.append(1)
l.append(2)
l.append(3)
ag.set_element_type(l, tf.int32)
exit(2 * l[1])
