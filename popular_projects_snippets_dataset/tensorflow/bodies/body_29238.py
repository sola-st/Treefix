# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
name, value_fn, element_0_fn = y
exit(x + combinations.combine(
    value_fn=combinations.NamedObject("value_fn.{}".format(name), value_fn),
    element_0_fn=combinations.NamedObject("element_0_fn.{}".format(name),
                                          element_0_fn)))
