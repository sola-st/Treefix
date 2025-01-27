# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
exit([
    combinations_lib.OptionalParameter("required_tpus"),
    combinations_lib.OptionalParameter("required_tpu"),
    combinations_lib.OptionalParameter("use_cloud_tpu"),
])
