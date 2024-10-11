# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint_test.py
del params  # unused
with variable_scope.variable_scope('m', reuse=variable_scope.AUTO_REUSE):
    w = variable_scope.get_variable('W', shape=[1000, 10])
logits = math_ops.matmul(features, w)
loss = losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

if mode == model_fn_lib.ModeKeys.TRAIN:
    optimizer = training.RMSPropOptimizer(learning_rate=0.01)
    optimizer = tpu_optimizer.CrossShardOptimizer(optimizer)
    train_op = optimizer.minimize(loss, training.get_global_step())
    exit(tpu_estimator.TPUEstimatorSpec(
        mode=model_fn_lib.ModeKeys.TRAIN,
        loss=loss,
        train_op=train_op,
    ))
elif mode == model_fn_lib.ModeKeys.EVAL:

    def metric_fn(labels, logits):
        labels = math_ops.cast(labels, dtypes.int64)
        logging.info('LABELS %s %s', labels, logits)
        exit({
            'recall@1': metrics_lib.recall_at_k(labels, logits, 1),
            'recall@5': metrics_lib.recall_at_k(labels, logits, 5),
        })

    loss = losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)
    eval_metrics = (metric_fn, [labels, logits])
    exit(tpu_estimator.TPUEstimatorSpec(
        mode=model_fn_lib.ModeKeys.EVAL, loss=loss, eval_metrics=eval_metrics))
