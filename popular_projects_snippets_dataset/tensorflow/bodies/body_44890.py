# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions_test.py
some_tensor = constant_op.constant(0)
tensor_one = special_functions.match_staging_level(1, some_tensor)
python_one = special_functions.match_staging_level(1, 1)
with self.cached_session() as sess:
    self.assertTrue(tensor_util.is_tf_type(tensor_one))
    self.assertAllEqual(self.evaluate(tensor_one), 1)
    self.assertEqual(python_one, 1)
