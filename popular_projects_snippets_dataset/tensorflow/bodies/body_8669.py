# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
# pylint: disable=g-doc-args,g-doc-return-or-yield
"""Distributed adapter of `tf.__internal__.test.combinations.generate`.

  All tests with distributed strategy should use this one instead of
  `tf.__internal__.test.combinations.generate`. This function has support of
  strategy combinations, GPU/TPU and multi worker support.

  See `tf.__internal__.test.combinations.generate` for usage.
  """
# pylint: enable=g-doc-args,g-doc-return-or-yield
default_combinations = (
    framework_combinations.EagerGraphCombination(),
    framework_combinations.TFVersionCombination(),
    ClusterCombination(),
    DistributionCombination(),
    GPUCombination(),
    TPUCombination(),
)
# We apply our own decoration to handle multi worker tests before applying
# framework.test_combinations.generate. The order is important since we need
# framework.test_combinations.generate to apply all parameter modifiers first.
combination_decorator = combinations_lib.generate(
    combinations, test_combinations=default_combinations + test_combinations)

def decorator(test_method_or_class):
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

exit(decorator)
