# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
debugged_graph = debug_events_reader.DebuggedGraph(
    None,
    "b1c2",
    outer_graph_id=None,
)
self.assertEqual(
    debugged_graph.to_json(), {
        "name": None,
        "graph_id": "b1c2",
        "outer_graph_id": None,
        "inner_graph_ids": [],
    })
