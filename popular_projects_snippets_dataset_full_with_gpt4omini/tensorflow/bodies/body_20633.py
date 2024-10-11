# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/datasets_test.py
for i in range(len(proto_with_symbolic_values.dim)):
    if proto_with_symbolic_values.dim[i].size < -1:
        proto_with_symbolic_values.dim[i].size = -1
exit(tensor_shape.TensorShape(proto_with_symbolic_values))
