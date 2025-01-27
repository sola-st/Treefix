# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with self.assertRaises(RuntimeError) as cm:
    op_def_library.apply_op("unknown")
self.assertEqual(str(cm.exception), "Unrecognized Op name unknown")
