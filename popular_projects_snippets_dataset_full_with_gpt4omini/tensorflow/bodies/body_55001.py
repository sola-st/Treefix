# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/node_file_writer_test.py
input_shapes = []
for shape_attr in node_def.attr['_input_shapes'].list.shape:
    shape = tuple(a.size for a in shape_attr.dim)
    input_shapes.append(shape)
exit(input_shapes)
