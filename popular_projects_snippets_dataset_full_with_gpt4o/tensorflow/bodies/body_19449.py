# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
num_replicas = strategy.num_replicas_in_sync

# Unpack the values `strategy.run()` returns.
loss = self._unpack(strategy, shard_out_val[0])
activation_watched = self._unpack(strategy, shard_out_val[1])
activation_favorited = self._unpack(strategy, shard_out_val[2])
activation_friends = self._unpack(strategy, shard_out_val[3])

# Core 0:
# Calculate the values of embedding activations.
activation_watched_gold0 = np.array([[0, 1, 2, 3], [4, 6, 8, 10]])
activation_favorited_gold0 = np.array([[4, 6, 8, 10], [4, 5, 6, 7]])
# Second row of `activation_friends_gold0` is the mean of the following.
# row 0: 0 1
# row 1: 2 3
# row 2: 4 5
activation_friends_gold0 = np.array([[6, 7], [2, 3]])

loss_gold0 = self._compute_loss(activation_watched_gold0,
                                activation_favorited_gold0,
                                activation_friends_gold0)

# Add on values from other cores:
# Activations for watched are an alternating sequence of
# activation_watched_gold0 and activation_favorited_gold0.
# For favorited it is the same but in the opposite order.
activation_watched_gold = np.concatenate(
    (activation_watched_gold0, activation_favorited_gold0))
activation_favorited_gold = np.concatenate(
    (activation_favorited_gold0, activation_watched_gold0))
activation_friends_gold = np.concatenate(
    (activation_friends_gold0, activation_friends_gold0))

if is_high_dimensional:
    activation_watched_gold = np.stack([activation_watched_gold] *
                                       self.batch_size * num_replicas)

    activation_favorited_gold = np.stack([activation_favorited_gold] *
                                         self.batch_size * num_replicas)

    activation_friends_gold = np.stack([activation_friends_gold] *
                                       self.batch_size * num_replicas)
else:
    if num_replicas == 1:
        activation_watched_gold = activation_watched_gold0
        activation_favorited_gold = activation_favorited_gold0
        activation_friends_gold = activation_friends_gold0
    else:
        activation_watched_gold = np.concatenate(
            [activation_watched_gold] * (num_replicas // self.batch_size))
        activation_favorited_gold = np.concatenate(
            [activation_favorited_gold] * (num_replicas // self.batch_size))
        activation_friends_gold = np.concatenate(
            [activation_friends_gold] * (num_replicas // self.batch_size))

loss_gold = [loss_gold0] * num_replicas

# Test values.
self.assertAllClose(activation_watched_gold, activation_watched)
self.assertAllClose(activation_favorited_gold, activation_favorited)
self.assertAllClose(activation_friends_gold, activation_friends)

self.assertAllClose(loss_gold, loss)

embedding_table_video_before = np.copy(
    np.reshape(self.embedding_values, [8, 4]))
embedding_table_user_before = np.copy(
    np.reshape(self.embedding_values, [16, 2]))
if is_high_dimensional:
    global_batch_size = self.batch_size * self.data_batch_size * num_replicas
else:
    global_batch_size = self.batch_size * num_replicas
if training:
    gradient_wrt_watched_gold = (2 * activation_watched_gold /
                                 global_batch_size)
    gradient_wrt_favorited_gold = (2 * activation_favorited_gold /
                                   global_batch_size)
    gradient_wrt_friends_gold = (2 * activation_friends_gold /
                                 global_batch_size)

    # Calculate gradients wrt embedding tables.
    gradients_wrt_user = (
        self._compute_gradients_wrt_embedding_table(
            gradient_wrt_friends_gold, embedding_table_user_before,
            input_data[2].indices.numpy(), input_data[2].values.numpy(),
            self.table_user.combiner))
    gradients_wrt_video = (
        self._compute_gradients_wrt_embedding_table(
            gradient_wrt_favorited_gold, embedding_table_video_before,
            input_data[1].indices.numpy(), input_data[1].values.numpy(),
            self.table_video.combiner) +
        self._compute_gradients_wrt_embedding_table(
            gradient_wrt_watched_gold, embedding_table_video_before,
            input_data[0].indices.numpy(), input_data[0].values.numpy(),
            self.table_video.combiner))

    self._check_embedding_and_slot_variables(embedding_table_user_before,
                                             gradients_wrt_user,
                                             embedding_table_video_before,
                                             gradients_wrt_video, optimizer,
                                             table_to_variable)
