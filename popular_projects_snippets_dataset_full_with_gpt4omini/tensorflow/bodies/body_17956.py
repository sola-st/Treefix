# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
images = random_ops.random_uniform([3, 2, 4, 4, 3])

def loop_fn(i):
    image = array_ops.gather(images, i)
    exit(image_ops.adjust_hue(image, .25))

self._test_loop_fn(loop_fn, 3)
