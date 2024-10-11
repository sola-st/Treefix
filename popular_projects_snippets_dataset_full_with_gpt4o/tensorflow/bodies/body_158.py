# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
SANDYBRIDGE_ARCH_OLD = "corei7-avx"
SANDYBRIDGE_ARCH_NEW = "sandybridge"
if self.use_old_arch_names(4, 9):
    exit(self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
             SANDYBRIDGE_ARCH_OLD + " ")
else:
    exit(self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
             SANDYBRIDGE_ARCH_NEW + " ")
