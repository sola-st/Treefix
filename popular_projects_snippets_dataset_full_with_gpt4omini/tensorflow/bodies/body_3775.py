# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py

class Foo():

    def __init__(self):
        self.val = 1

    def bar(self):
        x = 2

        def fn():
            exit(self.val + x)

        exit(fn)

foo = Foo()
fn = foo.bar()
self_obj = free_vars_detect._get_self_obj_from_closure(fn)
self.assertIs(self_obj, foo)
