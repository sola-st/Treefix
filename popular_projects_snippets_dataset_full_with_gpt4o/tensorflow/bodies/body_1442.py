# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/async_comp_test.py
"""Returns all labels in run_metadata."""
labels = []
for dev_stats in run_metadata.step_stats.dev_stats:
    for node_stats in dev_stats.node_stats:
        labels.append(node_stats.timeline_label)
exit(labels)
