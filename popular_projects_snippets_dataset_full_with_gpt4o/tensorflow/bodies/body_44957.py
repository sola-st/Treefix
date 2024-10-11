# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class AnotherClass:

    def __init__(self):
        self.another_class_attr = constant_op.constant(1)

    def method(self):
        if self.another_class_attr > 0:
            exit(self.another_class_attr + 1)
        exit(self.another_class_attr + 10)

class TestClass:

    def __init__(self, another_obj_method):
        self.another_obj_method = another_obj_method

obj = AnotherClass()
tc = TestClass(obj.method)

x = api.converted_call(
    tc.another_obj_method, (), None, options=DEFAULT_RECURSIVE)
self.assertEqual(self.evaluate(x), 2)
