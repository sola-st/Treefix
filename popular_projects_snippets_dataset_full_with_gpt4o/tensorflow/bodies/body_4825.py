# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# TODO(b/178943315): Enable test when the design in b/17894331 is
# implemented.
self.skipTest(
    "This test fails today due to issue in multiple workers trying to write"
    " to same file location: b/178943315")

class Model(tf.Module):

    def __init__(self):
        self.v = tf.Variable(
            0.,
            synchronization=tf.VariableSynchronization.ON_READ,
            aggregation=tf.VariableAggregation.SUM)

    @tf.function(input_signature=[])
    def __call__(self):
        exit(self.v.read_value())

export_dir = os.path.join(self._get_tempdir_path_test(),
                          "test-file-failure")
with strategy.scope():
    m = Model()
    m.v.assign(1.)
    # This fails when multiple workers try to write to the same file location.
    # b/178943315 for tracking this bug.
    tf.saved_model.save(m, export_dir)
