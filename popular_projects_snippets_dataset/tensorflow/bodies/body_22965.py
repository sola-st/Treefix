# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
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
