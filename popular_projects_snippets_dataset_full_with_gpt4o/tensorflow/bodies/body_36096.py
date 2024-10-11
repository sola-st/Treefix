# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.cached_session():
    v = resource_variable_ops.ResourceVariable(1.0)
    self.evaluate(variables.global_variables_initializer())

    w = resource_variable_ops.ResourceVariable.from_proto(v.to_proto())
    self.assertEqual(2, math_ops.add(w, 1).eval())

    self.assertEqual(v._handle, w._handle)
    self.assertEqual(v._graph_element, w._graph_element)
