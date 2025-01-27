# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

class DeviceSettingThread(self.TestThread):

    def run(self):
        with g.device("/job:worker/replica:{}".format(self._replica_id)):
            self.has_mutated_graph.set()
            self.should_continue.wait()
            self.should_continue.clear()
            g.create_op(
                "FloatOutput", [], [dtypes.float32],
                name="FloatOutput_{}".format(self._replica_id))

g = ops.Graph()
# If `switch_to_thread` isn't called, then device placement of the ops
# below is not deterministic.
g.switch_to_thread_local()
threads = [DeviceSettingThread(g, i) for i in range(3)]
for t in threads:
    t.start()
    t.has_mutated_graph.wait()
    t.has_mutated_graph.clear()
for t in threads:
    t.should_continue.set()
    t.join()

gd = g.as_graph_def()
self.assertProtoEqualsVersion("""
      node { name: "FloatOutput_0" op: "FloatOutput"
             device: "/job:worker/replica:0" }
      node { name: "FloatOutput_1" op: "FloatOutput"
             device: "/job:worker/replica:1" }
      node { name: "FloatOutput_2" op: "FloatOutput"
             device: "/job:worker/replica:2" }
    """, gd)
