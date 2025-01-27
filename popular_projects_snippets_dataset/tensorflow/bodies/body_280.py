# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
initializers = [
    "zeros",
    "ones",
    "constant",
    "random_uniform",
    "random_normal",
    "truncated_normal",
    "variance_scaling",
    "orthogonal",
    "glorot_uniform",
    "glorot_normal",
    "identity",
    "lecun_normal",
    "lecun_uniform",
    "he_normal",
    "he_uniform",
]
self.verify_compat_v1_rename_correctness(
    initializers, ns_prefix="initializers")

initializers = [
    "zeros_initializer",
    "ones_initializer",
    "constant_initializer",
    "random_uniform_initializer",
    "random_normal_initializer",
    "truncated_normal_initializer",
    "variance_scaling_initializer",
    "orthogonal_initializer",
    "glorot_uniform_initializer",
    "glorot_normal_initializer",
]
self.verify_compat_v1_rename_correctness(initializers)

initializers = [
    "zeros",
    "ones",
    "Ones",
    "Zeros",
    "constant",
    "Constant",
    "VarianceScaling",
    "Orthogonal",
    "orthogonal",
    "Identity",
    "identity",
    "glorot_uniform",
    "glorot_normal",
    "lecun_normal",
    "lecun_uniform",
    "he_normal",
    "he_uniform",
    "TruncatedNormal",
    "truncated_normal",
    "RandomUniform",
    "uniform",
    "random_uniform",
    "RandomNormal",
    "normal",
    "random_normal",
]
self.verify_compat_v1_rename_correctness(
    initializers, ns_prefix="keras.initializers")
