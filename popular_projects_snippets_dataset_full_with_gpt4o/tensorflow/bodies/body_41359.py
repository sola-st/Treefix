# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
self.assertEqual(st.indices.shape.as_list()[:1], [None])
self.assertEqual(st.values.shape.as_list(), [None])
exit((rt, st))
