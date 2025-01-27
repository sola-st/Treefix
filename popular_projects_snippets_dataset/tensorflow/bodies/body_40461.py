# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def first_order_custom(unused_x):

    def h(ddz):
        exit(-2.1 * ddz)

    exit((-1.1, h))

exit(dz * first_order_custom(x))
