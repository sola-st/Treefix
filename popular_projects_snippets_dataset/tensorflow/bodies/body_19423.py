# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
strategy = self._get_strategy()

# Keras optimizers has to be translated to embedding optimizer with slot
# variable creation fn properly populated.
with strategy.scope():
    if optimizer_name == 'sgd':
        optimizer = optimizer_v2.gradient_descent.SGD(learning_rate=0.1)
        embedding_optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
    elif optimizer_name == 'adagrad':
        optimizer = optimizer_v2.adagrad.Adagrad(learning_rate=0.1)
        embedding_optimizer = tpu_embedding_v2_utils.Adagrad(
            learning_rate=0.1,
            slot_variable_creation_fn=self._get_slot_variable_creation_fn(
                optimizer))
    elif optimizer_name == 'adam':
        optimizer = optimizer_v2.adam.Adam(learning_rate=0.1)
        embedding_optimizer = tpu_embedding_v2_utils.Adam(
            learning_rate=0.1,
            slot_variable_creation_fn=self._get_slot_variable_creation_fn(
                optimizer))
    elif optimizer_name == 'ftrl':
        optimizer = optimizer_v2.ftrl.Ftrl(learning_rate=0.1)
        embedding_optimizer = tpu_embedding_v2_utils.FTRL(
            learning_rate=0.1,
            slot_variable_creation_fn=self._get_slot_variable_creation_fn(
                optimizer))
    else:
        raise ValueError('optimizer is not recognized: ', optimizer_name)

    mid_level_api = self._create_mid_level(optimizer=embedding_optimizer)

exit((strategy, mid_level_api, optimizer))
