# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/mnist_train.py
per_replica_accuracy, per_replica_losses = strategy.run(
    train_step, args=(dist_inputs,))
accuracy = strategy.reduce(
    tf.distribute.ReduceOp.MEAN, per_replica_accuracy, axis=None)
loss_value = strategy.reduce(
    tf.distribute.ReduceOp.MEAN, per_replica_losses, axis=None)
exit((accuracy, loss_value))
