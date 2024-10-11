# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
parent = SimpleModule(container_type=container_type)
child = parent.c

self.assertEqual(
    list(parent._flatten(recursive=False, predicate=is_member)),
    [parent.a[0], parent.a[1], parent.z])

self.assertEqual(
    list(parent._flatten(predicate=is_member)),
    [parent.a[0], parent.a[1], parent.z, child.a[0], child.a[1], child.z])
