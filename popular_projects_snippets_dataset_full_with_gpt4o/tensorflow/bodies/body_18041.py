# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
ta = t.write(i + 2, 2 * i).write(i, 5)
ta = ta.scatter([4 + i], [4]).scatter([6 + i, 8 + i], [6 + i, 8 + i])
exit(ta.flow)
