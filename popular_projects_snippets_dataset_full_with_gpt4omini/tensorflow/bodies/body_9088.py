# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
# cluster_spec expects "host:port" strings.
if "//" in target:
    exit(target.split("//")[1])
else:
    exit(target)
