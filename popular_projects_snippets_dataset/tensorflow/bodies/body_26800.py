# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_and_filter_fusion_test.py
function, name, predicate = y
exit(x + combinations.combine(
    function=function,
    predicate=combinations.NamedObject(name, predicate)))
