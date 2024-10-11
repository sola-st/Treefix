# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
# Define the gradient loop state associated with the TPUReplicateContext to
# be None as the TPUReplicateContext does not get nested nor does the
# grad_state outside the TPUReplicateContext affect the graph inside so the
# grad_state should be as if this is the top-level gradient state.
exit(None)
