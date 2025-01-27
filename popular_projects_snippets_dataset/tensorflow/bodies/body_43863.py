# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_list_test.py
mat = []
ag.set_element_type(mat, tf.int32)
for _ in range(m):
    l = []
    ag.set_element_type(l, tf.int32)
    for j in range(n):
        l.append(j)
    mat.append(ag.stack(l, strict=False))
exit(ag.stack(mat, strict=False))
