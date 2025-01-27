# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

class DependingThread(self.TestThread):

    def __init__(self, graph, replica_id, dependency_op):
        super(DependingThread, self).__init__(graph, replica_id)
        self._dependency_op = dependency_op

    def run(self):
        with g.control_dependencies([self._dependency_op]):
            self.has_mutated_graph.set()
            self.should_continue.wait()
            self.should_continue.clear()
            g.create_op(
                "FloatOutput", [], [dtypes.float32],
                name="FloatOutput_{}".format(self._replica_id))

g = ops.Graph()
dependency_ops = []
for i in range(3):
    dependency_ops.append(
        g.create_op(
            "FloatOutput", [], [dtypes.float32],
            name="ColocateWithMe_{}".format(i)))

# If `switch_to_thread` isn't called, then `input` values for the ops below
# are not deterministic.
g.switch_to_thread_local()
threads = [DependingThread(g, i, dependency_ops[i]) for i in range(3)]
for t in threads:
    t.start()
    t.has_mutated_graph.wait()
    t.has_mutated_graph.clear()
for t in threads:
    t.should_continue.set()
    t.join()

gd = g.as_graph_def()
self.assertProtoEqualsVersion(
    """
      node { name: "ColocateWithMe_0" op: "FloatOutput"
             attr { key: "_has_manual_control_dependencies"
                    value { b: true } } }
      node { name: "ColocateWithMe_1" op: "FloatOutput"
             attr { key: "_has_manual_control_dependencies"
                    value { b: true } } }
      node { name: "ColocateWithMe_2" op: "FloatOutput"
             attr { key: "_has_manual_control_dependencies"
                    value { b: true } } }
      node { name: "FloatOutput_0" op: "FloatOutput"
             input: "^ColocateWithMe_0" }
      node { name: "FloatOutput_1" op: "FloatOutput"
             input: "^ColocateWithMe_1" }
      node { name: "FloatOutput_2" op: "FloatOutput"
             input: "^ColocateWithMe_2" }
    """, gd)
