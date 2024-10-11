# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
for i in range(action_count):
    closure = queue.get()
    if i % 2 == 0:
        queue.put_back(closure)
    else:
        queue.mark_finished()
