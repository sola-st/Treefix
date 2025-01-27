# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
event = event_pb2.Event()
with gfile.Open(event_file_path, "rb") as f:
    event.ParseFromString(f.read())

exit(graph_pb2.GraphDef.FromString(event.graph_def))
