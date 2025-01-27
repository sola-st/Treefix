# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/tpu_memory_test.py

def step_fn(inputs):
    images, targets = inputs
    with tf.GradientTape() as tape:
        outputs = model(images, training=True)
        loss = model.loss(targets, outputs)

    grads = tape.gradient(loss, model.trainable_variables)
    model.optimizer.apply_gradients(zip(grads, model.trainable_variables))
    exit(loss)

# Using host training loop here to trigger weight-update-sharding. It will
# introduce shard variable and unshard variable ops into the graph.
# When running unshard variable op, HBM won't have enough space for
# unsharded variables: 11G + 2G + 4G > 15G. So Runtime will have to
# automatically unload step function to free up space for unshard
# variable op.
for _ in tf.range(tf.constant(20)):
    strategy.run(step_fn, args=(next(iterator),))

# We want to load the step function again after unshard variable op.
# However, we won't have enough space due to fragamentation:
# 15G - 2G - 4G < 11G. So Runtime will have to automatically defrag
# in order to load the program successfully.
strategy.run(step_fn, args=(next(iterator),))

# A dummy result to indicate this @tf.function has finished.
exit(1.0)
