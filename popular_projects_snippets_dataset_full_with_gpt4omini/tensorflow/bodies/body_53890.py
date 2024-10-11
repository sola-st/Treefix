# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Sets graph.graph_def_versions.producer to `producer_version`."""
# The C API doesn't expose altering GraphDefVersions. We can indirectly set
# it via import_graph_def though.
graph_def = graph_pb2.GraphDef()
graph_def.versions.producer = producer_version
with graph.as_default():
    importer.import_graph_def(graph_def)
assert graph.graph_def_versions.producer, producer_version
