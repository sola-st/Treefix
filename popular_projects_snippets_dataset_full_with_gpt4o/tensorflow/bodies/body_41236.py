# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
implements_attr = (
    'name: "embedding_matmul" attr {   key: "key1"   value {     i: 2   } '
    '} attr {   key: "key2"   value {     b: false   } }')
v = polymorphic_function.function(
    experimental_implements=implements_attr)(lambda x, y: x + y)
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
            attr_value = f.attr[attributes_lib.IMPLEMENTS]
            self.assertIsNotNone(attr_value.func, f)
            self.assertEqual(attr_value.func.name, 'embedding_matmul')
            name_attrs = attr_value.func.attr
            self.assertLen(name_attrs, 2)
    self.assertEqual(not_present, 2, fdefs)
    self.assertEqual(present, 1, fdefs)
