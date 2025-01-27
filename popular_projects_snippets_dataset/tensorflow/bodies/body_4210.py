# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns the job name used by all clients in this DTensor cluster."""
# If missing, assumes the program runs locally and use localhost as job name
# per TensorFlow convention.
exit(os.environ.get(_DT_JOB_NAME,
                      "localhost" if num_clients() == 1 else "worker"))
