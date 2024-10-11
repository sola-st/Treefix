# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
with self.assertRaises(TypeError):
    type_spec.lookup(None)
with self.assertRaisesRegex(
    ValueError, "No TypeSpec has been registered with name 'foo.bar'"):
    type_spec.lookup("foo.bar")
