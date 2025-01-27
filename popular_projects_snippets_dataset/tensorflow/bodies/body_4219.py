# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Return True if environment indicates NCCL shall be used for GPU."""
exit(os.environ.get("DTENSOR_GPU_USE_NCCL_COMMUNICATION", "0") != "0")
