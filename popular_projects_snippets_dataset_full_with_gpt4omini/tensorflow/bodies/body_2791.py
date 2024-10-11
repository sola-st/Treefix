# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/mnist_train_test.py
accuracy = mnist_train.main(strategy)
self.assertGreater(accuracy, 0.7, 'accuracy sanity check')
