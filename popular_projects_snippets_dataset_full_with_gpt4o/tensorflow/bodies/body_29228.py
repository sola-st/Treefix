# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
name, value1_fn, value2_fn, value3_fn = y
exit(x + combinations.combine(
    value1_fn=combinations.NamedObject("value1_fn.{}".format(name),
                                       value1_fn),
    value2_fn=combinations.NamedObject("value2_fn.{}".format(name),
                                       value2_fn),
    value3_fn=combinations.NamedObject("value3_fn.{}".format(name),
                                       value3_fn)))
