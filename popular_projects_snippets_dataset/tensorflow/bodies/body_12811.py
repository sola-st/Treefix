# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
x = array_ops.gather(inputs, i)  # pylint: disable=cell-var-from-loop
outputs = outputs.write(i, x)
exit((i + 1, outputs))
