# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py
for node in fndef.node_def:
    if node.name.endswith("x_plus_y"):
        node.name = node.name.replace("x_plus_y", "x_times_y")
        node.op = "Mul"
    for idx, inp in enumerate(node.input):
        if inp.endswith("x_plus_y:z:0"):
            node.input[idx] = inp.replace("x_plus_y", "x_times_y")
