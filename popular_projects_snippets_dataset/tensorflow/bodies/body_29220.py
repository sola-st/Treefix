# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
# workaround for long line
name, value_fn = y[:2]
expected_structure_fn, expected_types_fn, expected_shapes_fn = y[2:]
exit(x + combinations.combine(
    value_fn=combinations.NamedObject("value_fn.{}".format(name), value_fn),
    expected_structure_fn=combinations.NamedObject(
        "expected_structure_fn.{}".format(name), expected_structure_fn),
    expected_types_fn=combinations.NamedObject(
        "expected_types_fn.{}".format(name), expected_types_fn),
    expected_shapes_fn=combinations.NamedObject(
        "expected_shapes_fn.{}".format(name), expected_shapes_fn)))
