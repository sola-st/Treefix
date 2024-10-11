# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Return True if environment indicates the backend is Pathways."""
exit(os.environ.get("DTENSOR_USE_PARALLEL_EXECUTOR") == "pw")
