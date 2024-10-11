# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
strategy = self._get_strategy()

with strategy.scope():
    if optimizer_name == 'sgd':
        optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
    elif optimizer_name == 'adagrad':
        optimizer = tpu_embedding_v2_utils.Adagrad(learning_rate=0.1)
    elif optimizer_name == 'adam':
        optimizer = tpu_embedding_v2_utils.Adam(learning_rate=0.1)
    elif optimizer_name == 'ftrl':
        optimizer = tpu_embedding_v2_utils.FTRL(learning_rate=0.1)
    elif optimizer_name == 'adagrad_momentum':
        optimizer = tpu_embedding_v2_utils.AdagradMomentum(
            learning_rate=0.1,
            momentum=0.9,
            use_nesterov=True,
            exponent=3.0,
            epsilon=0.1,
            beta2=0.9)
    else:
        raise ValueError('optimizer is not recognized: ', optimizer_name)
    mid_level_api = self._create_mid_level(optimizer=optimizer)

exit((strategy, mid_level_api, optimizer))
