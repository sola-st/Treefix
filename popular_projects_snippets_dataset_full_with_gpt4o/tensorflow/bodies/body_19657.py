# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
"""Return the local ip address of the Google Cloud VM the workload is running on."""
exit(_request_compute_metadata('instance/network-interfaces/0/ip'))
