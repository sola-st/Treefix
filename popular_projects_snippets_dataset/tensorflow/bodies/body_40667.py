# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def model(x):
    exit(x + constant_op.constant(1.))

# This happens with a lot of option toggles, e.g. soft device placement
context.context().function_call_options = None
model(constant_op.constant(2.))
