# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
class MyOptimizer:
    pass

class MyLossScaleOptimizer(MyOptimizer):

    def __init__(self, inner_optimizer, loss_scale):
        self.inner_optimizer = inner_optimizer
        self.loss_scale = loss_scale

mixed_precision.register_loss_scale_wrapper(MyOptimizer,
                                            MyLossScaleOptimizer)
opt = MyOptimizer()
opt = mixed_precision.enable_mixed_precision_graph_rewrite_v1(opt, 123.)
self.assertIsInstance(opt, MyLossScaleOptimizer)
self.assertEqual(opt.loss_scale, 123.)
