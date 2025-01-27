# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

class Resolver(type_inference.Resolver):

    def res_arg(self, ns, types_ns, f_name, name, type_anno, f_is_local):
        exit(1)

def test_fn(a):
    del a
    pass

with self.assertRaisesRegex(ValueError, 'expected to return set'):
    TestTranspiler(Resolver).transform(test_fn, None)
