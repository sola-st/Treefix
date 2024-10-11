# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util_test.py
a = array_ops.identity(1., name='a')
b = a + 1
c = array_ops.identity(2., name='c')
d = array_ops.identity(a + c, name='d')
with ops.control_dependencies([b]):
    e = array_ops.identity(3., name='e')
f = array_ops.identity(c + e, name='f')
exit((d, f))
