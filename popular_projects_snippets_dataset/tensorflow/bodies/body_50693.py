# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
meta_graph_def = meta_graph.create_meta_graph_def(
    graph_def=g.as_graph_def(add_shapes=has_shapes))

rr = self._EventsReader(test_dir)

# The first event should list the file_version.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual("brain.Event:2", ev.file_version)

# The next event should have the graph.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(0, ev.step)
ev_graph = graph_pb2.GraphDef()
ev_graph.ParseFromString(ev.graph_def)
self.assertProtoEquals(g.as_graph_def(add_shapes=has_shapes), ev_graph)

# The next event should have the metagraph.
ev = next(rr)
self.assertRecent(ev.wall_time)
self.assertEqual(0, ev.step)
ev_meta_graph = meta_graph_pb2.MetaGraphDef()
ev_meta_graph.ParseFromString(ev.meta_graph_def)
self.assertProtoEquals(meta_graph_def, ev_meta_graph)

# We should be done.
self.assertRaises(StopIteration, lambda: next(rr))
