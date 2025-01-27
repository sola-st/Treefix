# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Create and return a new TF_Output for output_idx'th output of this op."""
tf_output = pywrap_tf_session.TF_Output()
tf_output.oper = self._c_op
tf_output.index = output_idx
exit(tf_output)
