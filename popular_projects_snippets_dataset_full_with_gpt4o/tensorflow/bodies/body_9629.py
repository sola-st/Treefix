# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    a = constant_op.constant(1.0, shape=[1, 2])
    b = constant_op.constant(2.0, shape=[2, 3])
    c = math_ops.matmul(a, b)
    results_with_list = s.run([c])
    self.assertAllEqual([[4.0, 4.0, 4.0]], results_with_list[0])
    results_with_single = s.run(c)
    self.assertAllEqual([[4.0, 4.0, 4.0]], results_with_single)
    results_with_get = self.evaluate(c)
    self.assertAllEqual([[4.0, 4.0, 4.0]], results_with_get)
    a_val, b_val = s.run([a, b])  # Test multiple fetches.
    self.assertAllEqual([[1.0, 1.0]], a_val)
    self.assertAllEqual([[2.0, 2.0, 2.0], [2.0, 2.0, 2.0]], b_val)
    results_with_dict = s.run({'a': [a], 'b': b, 'z': [a, b]})
    self.assertAllEqual([[1.0, 1.0]], results_with_dict['a'][0])
    self.assertAllEqual([[2.0, 2.0, 2.0], [2.0, 2.0, 2.0]],
                        results_with_dict['b'])
    self.assertAllEqual(results_with_dict['a'][0], results_with_dict['z'][0])
    self.assertAllEqual(results_with_dict['b'], results_with_dict['z'][1])

    # Test nested structures
    results_with_nested_list = s.run([[[a, b], b], a, [a, b]])
    self.assertAllEqual([[1.0, 1.0]], results_with_nested_list[0][0][0])
    self.assertAllEqual([[2.0, 2.0, 2.0], [2.0, 2.0, 2.0]],
                        results_with_nested_list[0][0][1])
    self.assertAllEqual(results_with_nested_list[0][0][0],
                        results_with_nested_list[1])
    self.assertAllEqual(results_with_nested_list[1],
                        results_with_nested_list[2][0])
    self.assertAllEqual(results_with_nested_list[0][0][1],
                        results_with_nested_list[0][1])
    self.assertAllEqual(results_with_nested_list[0][1],
                        results_with_nested_list[2][1])
