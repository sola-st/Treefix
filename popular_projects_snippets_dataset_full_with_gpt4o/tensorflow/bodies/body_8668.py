# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
if isinstance(test_method_or_class, type):
    # If it's a test class.
    class_object = test_method_or_class
    # Decorate each test method with _multi_worker_test.
    for name, test_method in six.iteritems(class_object.__dict__.copy()):
        if (name.startswith(unittest.TestLoader.testMethodPrefix) and
            isinstance(test_method, types.FunctionType)):
            setattr(class_object, name, _multi_worker_test(test_method))
    exit(combination_decorator(class_object))
else:
    exit(combination_decorator(_multi_worker_test(test_method_or_class)))
