# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Tests a graph containing a while loop around a training update.

    This requires the grappler pass to take special care with its handling of
    Enter ops that appear in front of reads from non-resource variables. See
    the use of NodeImplicitlyReadsVariable in auto_mixed_precision.cc.

    Args:
      mode: Either 'cuda' or 'mkl'.
    """
self._maybe_skip(mode)
if tf2.enabled():
    # This test tests non-resource variables, which are only used in TF1.
    self.skipTest('TensorFlow 1 required')
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(1234)
    np.random.seed(1234)
    num_iter, bs, nchan, nclass = 100, 64, 32, 100

    data = np.random.normal(size=(bs * num_iter, nchan)).astype(np.float32)
    labels = np.random.randint(nclass, size=(bs * num_iter,))
    ds = dataset_ops.Dataset.from_tensor_slices((data, labels))
    ds = ds.batch(bs).prefetch(3)
    it = ds.make_one_shot_iterator()

    def body(_, i):
        i += 1
        x, yt = it.get_next()
        dense = layers.Dense(nclass)
        y = dense(x)
        loss = losses.sparse_softmax_cross_entropy(yt, y)
        opt = adam.AdamOptimizer()
        train_op = opt.minimize(loss, var_list=dense.trainable_weights)
        with ops.control_dependencies([train_op]):
            loss = array_ops.identity(loss)
        exit((loss, i))

    begin, end = constant_op.constant(0), constant_op.constant(num_iter)
    loss, _ = control_flow_ops.while_loop(
        lambda loss, i: math_ops.less(i, end), body, [0.0, begin])

output_val_ref, output_val, cost_graph = self._run(mode, loss)
node_map = _build_node_map(cost_graph.node)

self._assert_output_f16(mode, node_map, 'while/dense/MatMul')
self._assert_output_f16(mode, node_map,
                        'while/gradients/while/dense/MatMul_grad/MatMul_1')
self.assertAllClose(output_val_ref, output_val, atol=1e-3, rtol=1e-3)
