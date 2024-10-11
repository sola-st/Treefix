# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

class ColocatingThread(self.TestThread):

    def __init__(self, graph, replica_id, op_to_colocate_with):
        super(ColocatingThread, self).__init__(graph, replica_id)
        self._op_to_colocate_with = op_to_colocate_with

    def run(self):
        with g.colocate_with(self._op_to_colocate_with):
            self.has_mutated_graph.set()
            self.should_continue.wait()
            self.should_continue.clear()
            g.create_op(
                "FloatOutput", [], [dtypes.float32],
                name="FloatOutput_{}".format(self._replica_id))

g = ops.Graph()
ops_to_colocate_with = []
for i in range(3):
    with g.device("/job:worker/replica:{}".format(i)):
        ops_to_colocate_with.append(
            g.create_op(
                "FloatOutput", [], [dtypes.float32],
                name="ColocateWithMe_{}".format(i)))

    # If `switch_to_thread` isn't called, then `device` and `attr` values for
    # the ops below are not deterministic.
g.switch_to_thread_local()
threads = [
    ColocatingThread(g, i, ops_to_colocate_with[i]) for i in range(3)
]
for t in threads:
    t.start()
    t.has_mutated_graph.wait()
    t.has_mutated_graph.clear()
for t in threads:
    t.should_continue.set()
    t.join()

gd = g.as_graph_def()
self.assertProtoEqualsVersion("""
      node { name: "ColocateWithMe_0" op: "FloatOutput"
             device: "/job:worker/replica:0" }
      node { name: "ColocateWithMe_1" op: "FloatOutput"
             device: "/job:worker/replica:1" }
      node { name: "ColocateWithMe_2" op: "FloatOutput"
             device: "/job:worker/replica:2" }
      node { name: "FloatOutput_0" op: "FloatOutput"
             device: "/job:worker/replica:0"
             attr { key: "_class"
               value { list {
                 s: "loc:@ColocateWithMe_0"}}}}
      node { name: "FloatOutput_1" op: "FloatOutput"
             device: "/job:worker/replica:1"
             attr { key: "_class"
               value { list {
                 s: "loc:@ColocateWithMe_1"}}}}
      node { name: "FloatOutput_2" op: "FloatOutput"
             device: "/job:worker/replica:2"
             attr { key: "_class"
               value { list {
                 s: "loc:@ColocateWithMe_2"}}}}
    """, gd)
