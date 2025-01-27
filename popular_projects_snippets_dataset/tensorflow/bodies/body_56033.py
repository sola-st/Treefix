# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations.py
"""The decorator to be returned."""

# Generate good test names that can be used with --test_filter.
named_combinations = []
for combination in combinations:
    # We use OrderedDicts in `combine()` and `times()` to ensure stable
    # order of keys in each dictionary.
    assert isinstance(combination, OrderedDict)
    name = "".join([
        "_{}_{}".format("".join(filter(str.isalnum, key)),
                        "".join(filter(str.isalnum, _get_name(value, i))))
        for i, (key, value) in enumerate(combination.items())
    ])
    named_combinations.append(
        OrderedDict(
            list(combination.items()) +
            [("testcase_name", "_test{}".format(name))]))

if isinstance(test_method_or_class, type):
    class_object = test_method_or_class
    class_object._test_method_ids = test_method_ids = {}
    for name, test_method in class_object.__dict__.copy().items():
        if (name.startswith(unittest.TestLoader.testMethodPrefix) and
            isinstance(test_method, types.FunctionType)):
            delattr(class_object, name)
            methods = {}
            parameterized._update_class_dict_for_param_test_case(
                class_object.__name__, methods, test_method_ids, name,
                parameterized._ParameterizedTestIter(
                    _augment_with_special_arguments(
                        test_method, test_combinations=test_combinations),
                    named_combinations, parameterized._NAMED, name))
            for method_name, method in methods.items():
                setattr(class_object, method_name, method)

    exit(class_object)
else:
    test_method = _augment_with_special_arguments(
        test_method_or_class, test_combinations=test_combinations)
    exit(parameterized.named_parameters(*named_combinations)(test_method))
