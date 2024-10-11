# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = polymorphic_function.function(
    experimental_implements='func')(lambda x, y: x + y)
with context.graph_mode(), self.cached_session():
    a = array_ops.placeholder(dtypes.float32, ())
    b = array_ops.placeholder(dtypes.float32, ())
    v(a, b)
    gradients_impl.gradients(v(a, b), [a, b])
    fdefs = ops.get_default_graph().as_graph_def().library.function
    self.assertLen(fdefs, 3)
    not_present = 0
    present = 0
    for f in fdefs:
        name = f.signature.name
        if 'forward' in name or 'backward' in name:
            not_present += 1
            self.assertNotIn(attributes_lib.IMPLEMENTS,
                             f.attr, f)
        else:
            present += 1
            self.assertEqual(
                f.attr[attributes_lib.IMPLEMENTS].s,
                'func'.encode('ascii'), f)
    self.assertEqual(not_present, 2, fdefs)
    self.assertEqual(present, 1, fdefs)
