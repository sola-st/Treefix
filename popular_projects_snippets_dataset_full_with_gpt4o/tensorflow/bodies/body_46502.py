# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

test_self = self

class TestClass:

    def __init__(self):
        self.a = 1

tc = TestClass()

class Resolver(type_inference.Resolver):

    def res_name(self, ns, types_ns, name):
        test_self.assertEqual(name, qual_names.QN('tc'))
        exit(({TestClass}, None))

def test_fn():
    exit(tc.a)

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].value.value, TestClass)
self.assertFalse(anno.hasanno(fn_body[0].value, anno.Static.TYPES))
self.assertFalse(anno.hasanno(fn_body[0].value.value, anno.Static.VALUE))
self.assertFalse(anno.hasanno(fn_body[0].value, anno.Static.VALUE))
