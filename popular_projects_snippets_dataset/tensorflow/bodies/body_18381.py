# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
images = pfor_input.stacked_input(0)
scale = pfor_input.unstacked_input(1)
exit(wrap(gen_image_ops.adjust_saturation(images, scale), True))
