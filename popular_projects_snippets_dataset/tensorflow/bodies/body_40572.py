# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
weak_key_dict = weakref.WeakKeyDictionary()

strong_x = constant_op.constant([[1.]])
strong_y = constant_op.constant([[2.]])
strong_x_ref = strong_x.ref()
strong_y_ref = strong_y.ref()
weak_key_dict[strong_x_ref] = constant_op.constant([[3.]])
weak_key_dict[strong_y_ref] = constant_op.constant([[4.]])
strong_y.a = constant_op.constant([[5.]])
weak_x_ref = weakref.ref(strong_x)

del strong_x, strong_x_ref
self.assertIs(weak_x_ref(), None)
self.assertEqual([strong_y_ref], list(weak_key_dict))
self.assertLen(list(weak_key_dict), 1)
self.assertLen(weak_key_dict, 1)

del strong_y, strong_y_ref
self.assertEqual([], list(weak_key_dict))
