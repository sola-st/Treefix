# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
"""Function to generate parameterized inputs for testing."""
params = []
str_template = "_{}{}{}{}"
map_model_type = {
    "PostTraining": True,
    # "DuringTraining": False,
}
map_quantize_type_to_io_types = {
    tf.int8: {tf.float32, tf.int8, tf.uint8},
    tf.int16: {tf.float32, tf.int16}
}
for k1, v1 in map_model_type.items():
    for qtype, v2 in map_quantize_type_to_io_types.items():
        qstr = "_IntegerQuantize{}".format(qtype.name.capitalize())
        for itype in v2:
            istr = "_Input{}".format(itype.name.capitalize())
            for otype in v2:
                ostr = "_Output{}".format(otype.name.capitalize())
                params.append((str_template.format(k1, qstr, istr,
                                                   ostr), v1, qtype, itype, otype))
exit(params)
