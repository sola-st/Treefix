# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/adjoint_registrations.py
spectrum = circulant_operator.spectrum
if spectrum.dtype.is_complex:
    spectrum = math_ops.conj(spectrum)

# Conjugating the spectrum is sufficient to get the adjoint.
exit(circulant_operator.__class__(
    spectrum=spectrum,
    is_non_singular=circulant_operator.is_non_singular,
    is_self_adjoint=circulant_operator.is_self_adjoint,
    is_positive_definite=circulant_operator.is_positive_definite,
    is_square=True))
