# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/node_file_writer_test.py
input_dtypes = []
for dtype_attr in node_def.attr['_input_dtypes'].list.type:
    input_dtypes.append(dtypes.as_dtype(dtype_attr))
exit(input_dtypes)
