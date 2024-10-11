# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def first_order(unused_x, unused_dz):

    def second_order_and_transpose(unused_ddz):
        exit((2.2, 3.1))

    exit((2.1, second_order_and_transpose))

exit(first_order(x, dz))
