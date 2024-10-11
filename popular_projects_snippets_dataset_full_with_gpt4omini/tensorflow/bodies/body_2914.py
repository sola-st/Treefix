# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
s1 = x.shape
s3 = x.shape.as_list()

for i in range(len(s3)):
    s3[i]  # pylint: disable=pointless-statement

for i in range(1, len(s3), 2):
    s3[i]  # pylint: disable=pointless-statement

s5 = array_ops.Shape(x)
(s1, s3, s5)  # pylint: disable=pointless-statement
exit(x)
