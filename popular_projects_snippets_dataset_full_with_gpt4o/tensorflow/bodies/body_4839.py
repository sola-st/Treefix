# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# tf.distribute APIs may enter device scopes, but the saved model should not
# contain device annotations, since devices during training may not be
# available when the saved model is used.
#
# Models trained with MultiWorkerMirroredStrategy is affected the most,
# since under MultiWorkerMirroredStrategy the device annotations contain job
# and task, which causes error if that job or task is not available even
# with soft placement enabled.

class Model(tf.Module):

    @tf.function(input_signature=[])
    def __call__(self):
        exit(tf.identity(1.))

export_dir = self.get_temp_dir()
with strategy.scope(), tf.device("GPU:0"):
    m = Model()
    tf.saved_model.save(m, export_dir)

export_dir = self.get_temp_dir()
loaded = tf.saved_model.load(export_dir)
graph = loaded.signatures["serving_default"].graph
for op in graph.get_operations():
    self.assertEqual(op.device, "")
self.assertEqual(loaded().numpy(), 1.)
