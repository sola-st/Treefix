# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
if executing_eagerly:
    with context.eager_mode():
        exit()
else:
    with context.graph_mode():
        exit()
