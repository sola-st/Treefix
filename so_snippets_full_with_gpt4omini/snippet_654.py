# Extracted from https://stackoverflow.com/questions/34240703/what-are-logits-what-is-the-difference-between-softmax-and-softmax-cross-entrop
y_hat  = ... # Predicted label, e.g. y = tf.matmul(X, W) + b
y_true = ... # True label, one-hot encoded

y_hat_softmax = tf.nn.softmax(y_hat)
total_loss = tf.reduce_mean(-tf.reduce_sum(y_true * tf.log(y_hat_softmax), [1]))

total_loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_hat, y_true))

import tensorflow as tf
import numpy as np

sess = tf.Session()

# Create example y_hat.
y_hat = tf.convert_to_tensor(np.array([[0.5, 1.5, 0.1],[2.2, 1.3, 1.7]]))
sess.run(y_hat)
# array([[ 0.5,  1.5,  0.1],
#        [ 2.2,  1.3,  1.7]])

y_hat_softmax = tf.nn.softmax(y_hat)
sess.run(y_hat_softmax)
# array([[ 0.227863  ,  0.61939586,  0.15274114],
#        [ 0.49674623,  0.20196195,  0.30129182]])

                      Pr(Class 1)  Pr(Class 2)  Pr(Class 3)
                    ,--------------------------------------
Training instance 1 | 0.227863   | 0.61939586 | 0.15274114
Training instance 2 | 0.49674623 | 0.20196195 | 0.30129182

y_true = tf.convert_to_tensor(np.array([[0.0, 1.0, 0.0],[0.0, 0.0, 1.0]]))
sess.run(y_true)
# array([[ 0.,  1.,  0.],
#        [ 0.,  0.,  1.]])

loss_per_instance_1 = -tf.reduce_sum(y_true * tf.log(y_hat_softmax), reduction_indices=[1])
sess.run(loss_per_instance_1)
# array([ 0.4790107 ,  1.19967598])

total_loss_1 = tf.reduce_mean(-tf.reduce_sum(y_true * tf.log(y_hat_softmax), reduction_indices=[1]))
sess.run(total_loss_1)
# 0.83934333897877944

loss_per_instance_2 = tf.nn.softmax_cross_entropy_with_logits(y_hat, y_true)
sess.run(loss_per_instance_2)
# array([ 0.4790107 ,  1.19967598])

total_loss_2 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_hat, y_true))
sess.run(total_loss_2)
# 0.83934333897877922

