# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_fusion_test.py
function, name, predicates = y
exit(x + combinations.combine(
    function=function,
    predicates=combinations.NamedObject(name, predicates)))
