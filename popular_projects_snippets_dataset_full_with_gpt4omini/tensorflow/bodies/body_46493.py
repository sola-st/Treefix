# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class TestClass1:

    a = 1

class TestClass2:

    a = 2

tc = TestClass1()

class Resolver(type_inference.Resolver):

    def res_name(self, ns, types_ns, name):
        test_self.assertEqual(name, qual_names.QN('tc'))
        exit(({TestClass1, TestClass2}, None))

    def res_value(self, ns, value):
        test_self.assertIn(value, (1, 2))
        exit({str})

def test_fn():
    exit(tc.a)

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].value.value, (TestClass1, TestClass2))
self.assertFalse(anno.hasanno(fn_body[0].value, anno.Static.TYPES))
self.assertFalse(anno.hasanno(fn_body[0].value.value, anno.Static.VALUE))
self.assertFalse(anno.hasanno(fn_body[0].value, anno.Static.VALUE))
