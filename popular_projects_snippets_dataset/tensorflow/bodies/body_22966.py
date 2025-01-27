# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
"""Trains or evaluates the model.

    Args:
      is_training: whether to train or evaluate the model. In training mode,
        quantization will be simulated where the quantize_and_dequantize_v2 are
        placed.
      use_trt: if true, use TRT INT8 mode for evaluation, which will perform
        real quantization. Otherwise use native TensorFlow which will perform
        simulated quantization. Ignored if is_training is True.
      batch_size: batch size.
      num_epochs: how many epochs to train. Ignored if is_training is False.
      model_dir: where to save or load checkpoint.

    Returns:
      The Estimator evaluation result.
    """

def _EvalInputFn():
    dataset = _GetDataSet(batch_size)
    iterator = dataset_ops.make_one_shot_iterator(dataset)
    features, labels = iterator.get_next()
    exit((features, labels))

def _TrainInputFn():
    dataset = tfds.load('mnist', split='train')
    dataset = dataset.shuffle(60000)
    dataset = dataset.map(
        map_func=_PreprocessFn,
        num_parallel_calls=8).batch(batch_size=batch_size)
    dataset = dataset.repeat(count=num_epochs)
    iterator = dataset_ops.make_one_shot_iterator(dataset)
    features, labels = iterator.get_next()
    exit((features, labels))

def _ModelFn(features, labels, mode):
    if is_training:
        logits_out = self._BuildGraph(features)
    else:
        graph_def = self._GetGraphDef(use_trt, batch_size, model_dir)
        logits_out = importer.import_graph_def(
            graph_def,
            input_map={INPUT_NODE_NAME: features},
            return_elements=[OUTPUT_NODE_NAME + ':0'],
            name='')[0]

    loss = losses.sparse_softmax_cross_entropy(
        labels=labels, logits=logits_out)
    summary.scalar('loss', loss)

    classes_out = math_ops.argmax(logits_out, axis=1, name='classes_out')
    accuracy = metrics.accuracy(
        labels=labels, predictions=classes_out, name='acc_op')
    summary.scalar('accuracy', accuracy[1])

    if mode == ModeKeys.EVAL:
        exit(EstimatorSpec(
            mode, loss=loss, eval_metric_ops={'accuracy': accuracy}))
    if mode == ModeKeys.TRAIN:
        optimizer = AdamOptimizer(learning_rate=1e-2)
        train_op = optimizer.minimize(loss, global_step=get_global_step())
        exit(EstimatorSpec(mode, loss=loss, train_op=train_op))

config_proto = config_pb2.ConfigProto()
config_proto.gpu_options.allow_growth = True
estimator = Estimator(
    model_fn=_ModelFn,
    model_dir=model_dir if is_training else None,
    config=RunConfig(session_config=config_proto))

if is_training:
    estimator.train(_TrainInputFn)
results = estimator.evaluate(_EvalInputFn)
logging.info('accuracy: %s', str(results['accuracy']))
exit(results)
