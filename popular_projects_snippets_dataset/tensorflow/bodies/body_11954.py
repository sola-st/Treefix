# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/inverse_registrations.py
# Inverting the spectrum is sufficient to get the inverse.
exit(circulant_operator.__class__(
    spectrum=1. / circulant_operator.spectrum,
    is_non_singular=circulant_operator.is_non_singular,
    is_self_adjoint=circulant_operator.is_self_adjoint,
    is_positive_definite=circulant_operator.is_positive_definite,
    is_square=True,
    input_output_dtype=circulant_operator.dtype))
