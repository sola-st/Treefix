# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/random_seed_test.py
name, input_fn, output_fn = y
exit(x + combinations.combine(
    input_fn=combinations.NamedObject("input_fn.{}".format(name), input_fn),
    output_fn=combinations.NamedObject("output_fn.{}".format(name),
                                       output_fn)))
