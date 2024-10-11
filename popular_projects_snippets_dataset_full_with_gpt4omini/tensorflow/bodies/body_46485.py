# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class Resolver(type_inference.Resolver):

    def res_value(self, ns, value):
        test_self.assertEqual(value, tc.a)
        exit({int})

    def res_name(self, ns, types_ns, name):
        test_self.assertEqual(name, qual_names.QN('tc'))
        exit(({TestClass}, tc))

class TestClass:

    def __init__(self):
        self.a = 1

tc = TestClass()

def test_fn():
    exit(tc.a)

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].value.value, TestClass)
self.assertTypes(fn_body[0].value, int)
self.assertIs(anno.getanno(fn_body[0].value.value, anno.Static.VALUE), tc)
self.assertEqual(anno.getanno(fn_body[0].value, anno.Static.VALUE), tc.a)
