# Extracted from ./data/repos/tensorflow/tensorflow/cc/saved_model/testdata/generate_saved_models.py
self.v = variables.Variable(5.0)
loss = lambda: 3 * self.v
self.opt = adam.Adam()  # Should be tf.keras.optimizers.legacy.Adam. The
                        # new Keras optimizers do not have slot variables.

self.opt.minimize(loss, var_list=[self.v])
