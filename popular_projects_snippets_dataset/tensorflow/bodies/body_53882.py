# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
self.assertEqual(type(a), type(b))
if isinstance(a, (list, tuple)):
    self.assertLen(a, len(b), "Length differs for %s" % path)
    for i in range(len(a)):
        self._assertListCloseRecursive(a[i], b[i], rtol, atol, msg,
                                       "%s[%s]" % (path, i))
else:
    self._assertAllCloseRecursive(a, b, rtol, atol, path, msg)
