# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Runs the graph and returns the evaluation of the fetches."""
with session.Session(config=_get_config(None)) as sess:
    sess.run(variables.global_variables_initializer())
    output_val_ref = self.evaluate(fetches)

with session.Session(config=_get_config(mode)) as sess:
    sess.run(variables.global_variables_initializer())
    metadata = config_pb2.RunMetadata()
    output_val = sess.run(fetches, run_metadata=metadata)

exit((output_val_ref, output_val, metadata.cost_graph))
