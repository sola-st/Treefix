# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/draw_bounding_box_op_test.py
# Op only exists on GPU.
with self.cached_session(use_gpu=True):
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                "must be rank 4"):
        scores = constant_op.constant(
            value=[[[[1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0]]]])
        self.evaluate(
            image_ops.generate_bounding_box_proposals(
                scores=scores,
                bbox_deltas=[],
                image_info=[],
                anchors=[],
                pre_nms_topn=1))
