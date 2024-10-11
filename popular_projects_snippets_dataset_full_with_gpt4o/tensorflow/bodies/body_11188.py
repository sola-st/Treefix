# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Generate bounding box proposals from encoded bounding boxes.

  Args:
    scores: A 4-D float `Tensor` of shape
     `[num_images, height, width, num_achors]` containing scores of
      the boxes for given anchors, can be unsorted.
    bbox_deltas: A 4-D float `Tensor` of shape
     `[num_images, height, width, 4 x num_anchors]` encoding boxes
      with respect to each anchor. Coordinates are given
      in the form `[dy, dx, dh, dw]`.
    image_info: A 2-D float `Tensor` of shape `[num_images, 5]`
      containing image information Height, Width, Scale.
    anchors: A 2-D float `Tensor` of shape `[num_anchors, 4]`
      describing the anchor boxes.
      Boxes are formatted in the form `[y1, x1, y2, x2]`.
    nms_threshold: A scalar float `Tensor` for non-maximal-suppression
      threshold. Defaults to 0.7.
    pre_nms_topn: A scalar int `Tensor` for the number of
      top scoring boxes to be used as input. Defaults to 6000.
    min_size: A scalar float `Tensor`. Any box that has a smaller size
      than min_size will be discarded. Defaults to 16.
    post_nms_topn: An integer. Maximum number of rois in the output.
    name: A name for this operation (optional).

  Returns:
    rois: Region of interest boxes sorted by their scores.
    roi_probabilities: scores of the ROI boxes in the ROIs' `Tensor`.
  """
exit(gen_image_ops.generate_bounding_box_proposals(
    scores=scores,
    bbox_deltas=bbox_deltas,
    image_info=image_info,
    anchors=anchors,
    nms_threshold=nms_threshold,
    pre_nms_topn=pre_nms_topn,
    min_size=min_size,
    post_nms_topn=post_nms_topn,
    name=name))
