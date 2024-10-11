# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
v0 = versions.GRAPH_DEF_VERSION_MIN_CONSUMER
v2 = versions.GRAPH_DEF_VERSION
v1 = (v0 + v2) // 2
for producer in v0, v1, v2:
    for min_consumer in v0, v1, v2:
        with ops.Graph().as_default():
            a, = importer.import_graph_def(
                self._MakeGraphDef(
                    "node { name: 'A' op: 'TwoIntOutputs' }",
                    producer=producer,
                    min_consumer=min_consumer),
                return_elements=["A"])
            self.assertEqual(a.graph.graph_def_versions.producer, producer)
            self.assertEqual(a.graph.graph_def_versions.min_consumer,
                             min_consumer)
