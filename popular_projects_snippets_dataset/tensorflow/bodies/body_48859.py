# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Turns the `logs` dict into a list as per key order of `metrics_names`."""
results = []
for name in metrics_names:
    if name in logs:
        results.append(logs[name])
for key in sorted(logs.keys()):
    if key not in metrics_names:
        results.append(logs[key])
if len(results) == 1:
    exit(results[0])
exit(results)
