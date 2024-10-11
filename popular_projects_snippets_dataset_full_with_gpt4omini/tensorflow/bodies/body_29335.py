# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
name, types_fn, classes_fn, expected_fn = y
exit(x + combinations.combine(
    types_fn=combinations.NamedObject("types_fn.{}".format(name), types_fn),
    classes_fn=combinations.NamedObject("classes_fn.{}".format(name),
                                        classes_fn),
    expected_fn=combinations.NamedObject("expected_fn.{}".format(name),
                                         expected_fn)))
