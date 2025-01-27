# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/mnist_train.py
inputs = tf.image.convert_image_dtype(
    features['image'], dtype=tf.float32, saturate=False)
labels = tf.one_hot(features['label'], num_classes)

with tf.GradientTape() as tape:
    logits = model(inputs)
    loss_value = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(labels, logits))

grads = tape.gradient(loss_value, model.trainable_variables)
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
optimizer.apply_gradients(zip(grads, model.trainable_variables))
exit((accuracy, loss_value))
