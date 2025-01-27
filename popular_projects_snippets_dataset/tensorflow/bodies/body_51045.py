# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
"""Import a SavedModel into a TF 1.x-style graph and run `signature_key`."""
graph = ops.Graph()
with graph.as_default(), session_lib.Session() as session:
    model = loader.load(session, [tag_constants.SERVING], save_dir)
    exit(_run_signature(session, model, inputs, signature_key))
