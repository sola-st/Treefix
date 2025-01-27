# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
name, classes_fn, expected_fn = y
exit(x + combinations.combine(
    classes_fn=combinations.NamedObject("classes_fn.{}".format(name),
                                        classes_fn),
    expected_fn=combinations.NamedObject("expected_fn.{}".format(name),
                                         expected_fn)))
