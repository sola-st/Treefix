# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
nodedef = ops._NodeDef("None", "bar")
self.assertProtoEquals("op: 'None' name: 'bar'", nodedef)
