# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit({int})

    def res_list_literal(self, ns, elt_types):
        all_types = set()
        for s in elt_types:
            all_types |= s
        exit({List[t] for t in all_types})

def test_fn(a, b):
    exit([a, b])

node, _ = TestTranspiler(Resolver).transform(test_fn, None)
fn_body = node.body

self.assertTypes(fn_body[0].value, List[int])
self.assertTypes(fn_body[0].value.elts[0], int)
self.assertTypes(fn_body[0].value.elts[1], int)
