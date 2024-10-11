# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_system_metadata.py
exit(super(TPUSystemMetadata,
             cls).__new__(cls, num_cores, num_hosts, num_of_cores_per_host,
                          topology, devices))
