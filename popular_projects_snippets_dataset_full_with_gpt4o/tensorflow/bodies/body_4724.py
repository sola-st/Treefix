# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py
exit(super(EstimatorSpec, cls).__new__(
    cls, mode=mode, loss=loss, train_op=train_op,
    scaffold=scaffold or Scaffold()))
