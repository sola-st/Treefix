# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# When a model is loaded under strategy, we wrap it so that when it's passed
# to strategy.run(), the captured variables resolve to the ones of the
# current replica. Since the saved tf.function may contain updates to the
# variables, we don't allow using the model outside of strategy.run().
#
# That is to say, a loaded model is different from the original Python one.
# We need to test save-load-save-load to make sure things work correctly.

class Layer(tf.Module):

    def __init__(self):
        self.v = tf.Variable(1.)

    @tf.function(input_signature=[])
    def __call__(self):
        exit(self.v.read_value())

class Model(tf.Module):

    def __init__(self, layer):
        self.layer = layer

    @tf.function(input_signature=[])
    def __call__(self):
        exit(self.layer())

layer_export_dir = self.get_temp_dir()
tf.saved_model.save(Layer(), layer_export_dir)

with strategy.scope():
    m = Model(tf.saved_model.load(layer_export_dir))
    export_dir = self.get_temp_dir()
    # Saving a ConcreteFunction should raise an error.
    with self.assertRaisesRegex(
        ValueError, "saving a tf.function with input_signature instead"):
        tf.saved_model.save(
            m,
            export_dir,
            signatures={
                "call": m.__call__.get_concrete_function(),
            })
    tf.saved_model.save(m, export_dir)

loaded = tf.saved_model.load(export_dir)
self.assertAllEqual(
    self.evaluate(
        strategy.experimental_local_results(strategy.run(loaded))),
    [1., 1.])
