# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
debugged_graph = debug_events_reader.DebuggedGraph(
    "loss_function",
    "b1c2",
    outer_graph_id="a0b1",
)
debugged_graph.add_inner_graph_id("c2d3")
debugged_graph.add_inner_graph_id("c2d3e4")
self.assertEqual(
    debugged_graph.to_json(), {
        "name": "loss_function",
        "graph_id": "b1c2",
        "outer_graph_id": "a0b1",
        "inner_graph_ids": ["c2d3", "c2d3e4"],
    })
