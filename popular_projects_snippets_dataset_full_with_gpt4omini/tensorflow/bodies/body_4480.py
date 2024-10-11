# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/train_test.py
try:
    _ = tf.contrib
except AttributeError:
    test_method = unittest.skip(
        'This test requires tf.contrib:\n    `pip install tensorflow<=1.15`')(
            test_method)

exit(test_method)
