# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
name, original_value_fn, compatible_values_fn, incompatible_values_fn = y
exit(x + combinations.combine(
    original_value_fn=combinations.NamedObject(
        "original_value_fn.{}".format(name), original_value_fn),
    compatible_values_fn=combinations.NamedObject(
        "compatible_values_fn.{}".format(name), compatible_values_fn),
    incompatible_values_fn=combinations.NamedObject(
        "incompatible_values_fn.{}".format(name), incompatible_values_fn)))
