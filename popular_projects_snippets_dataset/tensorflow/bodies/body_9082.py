# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
exit(int(os.environ.get("TF_PS_HANDLE_UNKNOWN_ERROR", "0")) > 0)
