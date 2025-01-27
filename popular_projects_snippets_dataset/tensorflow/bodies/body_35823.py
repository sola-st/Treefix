# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
v = None

@def_function.function
def create_variable():
    with ops.name_scope("foo"):
        nonlocal v
        if v is None:
            v = variables.Variable(0.0, name="bar")
    self.assertEqual(v.name, "foo/bar:0")
with ops.get_default_graph().as_default():
    create_variable()
