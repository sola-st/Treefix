# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
# TODO(b/159186914): Remove the safeguard, and always set maximum_iterations.
if control_flow_util.GraphOrParentsInXlaContext(ops.get_default_graph()):
    opts['maximum_iterations'] = n
