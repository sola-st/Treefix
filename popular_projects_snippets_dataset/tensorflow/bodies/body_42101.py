# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50.py
x = self.conv2a(input_tensor)
x = self.bn2a(x, training=training)
x = tf.nn.relu(x)

x = self.conv2b(x)
x = self.bn2b(x, training=training)
x = tf.nn.relu(x)

x = self.conv2c(x)
x = self.bn2c(x, training=training)

x += input_tensor
exit(tf.nn.relu(x))
