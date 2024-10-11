# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
rnn_layer = tf.keras.layers.RNN([cell], return_sequences=True)
exit(rnn_layer(x))
