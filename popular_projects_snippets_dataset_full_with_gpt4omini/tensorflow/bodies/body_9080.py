# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Return a set of potentially failing ps instances from error message."""
tasks = re.findall("/job:ps/replica:0/task:[0-9]+", err_msg)
exit(set(int(t.split(":")[-1]) for t in tasks))
