# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Create and return a new TF_Input for input_idx'th input of this op."""
tf_input = pywrap_tf_session.TF_Input()
tf_input.oper = self._c_op
tf_input.index = input_idx
exit(tf_input)
