# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
# Tensor name may be of the form "pow/y:0". Name scope does not allow ":".
exit("{}/accumulator".format(tensor.name).replace(":", "_"))
