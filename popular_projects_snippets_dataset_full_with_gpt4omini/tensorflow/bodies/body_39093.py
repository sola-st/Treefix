# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
# gradient_checker_v2.computee_gradient doesn't take int32/int64.
# labels must be of type int32/int64, so passing them separately here.
exit(nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
    labels=labels, logits=logits, name="xent"))
