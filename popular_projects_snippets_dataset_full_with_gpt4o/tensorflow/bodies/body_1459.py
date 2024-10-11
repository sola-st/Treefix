# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
with session_lib.Session() as sess:

    # Check that calling the result as a compiled kernel doesn't crash.
    @function.Defun(compiled=True)
    def KernelWithNoOutputs():
        a = constant_op.constant(100)  # pylint: disable=unused-variable

    call = KernelWithNoOutputs()  # pylint: disable=assignment-from-no-return
    test_utils.RunWithWarmup(sess, call, {})
