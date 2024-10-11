# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
images = pfor_input.stacked_input(0)
delta = pfor_input.unstacked_input(1)
exit(wrap(gen_image_ops.adjust_hue(images, delta), True))
