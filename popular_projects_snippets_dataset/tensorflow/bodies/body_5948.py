# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations_test.py

@tf_function_1
def foo():
    self.assertFalse(context.executing_eagerly())

@tf_function_2
def bar():
    self.assertTrue(context.executing_eagerly())

foo()
bar()
