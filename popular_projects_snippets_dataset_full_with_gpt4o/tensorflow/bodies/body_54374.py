# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

class NameSettingThread(self.TestThread):

    def run(self):
        with g.name_scope("foo"):
            op1 = g.create_op("FloatOutput", [], [dtypes.float32])
            self.has_mutated_graph.set()
            self.should_continue.wait()
            self.should_continue.clear()
            op2 = g.create_op("FloatOutput", [], [dtypes.float32])
            self.result = (op1, op2)

g = ops.Graph()
threads = [NameSettingThread(g, i) for i in range(3)]
for t in threads:
    t.start()
    t.has_mutated_graph.wait()
    t.has_mutated_graph.clear()

for t in threads:
    t.should_continue.set()
    t.join()

suffixes = ["", "_1", "_2"]
for t, s in zip(threads, suffixes):
    self.assertEqual("foo" + s + "/FloatOutput", t.result[0].name)
    self.assertEqual("foo" + s + "/FloatOutput_1", t.result[1].name)
