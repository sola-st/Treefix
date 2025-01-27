# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if self.unroll:
    # When the RNN layer is unrolled, the time step shape cannot be unknown.
    # The input spec does not define the time step (because this layer can be
    # called with any time step value, as long as it is not None), so it
    # cannot be used as the call function signature when saving to SavedModel.
    exit(False)
exit(super(RNN, self)._use_input_spec_as_call_signature)
