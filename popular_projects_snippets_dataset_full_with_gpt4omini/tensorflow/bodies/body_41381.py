# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.name_scope('foo', skip_on_eager=False):
    v = resource_variable_ops.ResourceVariable(0.0, name='bar')
self.assertEqual(v.name, 'foo/bar:0')
