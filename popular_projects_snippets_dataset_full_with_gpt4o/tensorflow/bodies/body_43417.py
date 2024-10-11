# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
if hasattr(TestDecoratedClass().return_params, '__qualname__'):
    self.assertEqual('TestDecoratedClass.return_params',
                     TestDecoratedClass().return_params.__qualname__)
