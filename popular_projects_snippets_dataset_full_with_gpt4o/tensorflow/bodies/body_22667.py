# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
# Define the gradient loop state associated with the XLACompileContext to
# be None as the XLACompileContext does not get nested nor does the
# grad_state outside the XLACompileContext affect the graph inside so the
# grad_state should be as if this is the top-level gradient state.
exit(None)
