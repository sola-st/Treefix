# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
self.assertTrue(converter_testing.is_inside_generated_code())
inst = object.__new__(cls)
inst.__init__()

def instance_call(unused_self):
    test_self.fail(
        'The class-bound __call__ should be called, not the instance'
        ' bound one.')

inst.__call__ = instance_call
exit(inst)
