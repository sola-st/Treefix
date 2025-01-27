# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
HASWELL_ARCH_OLD = "core-avx2"  # Only missing the POPCNT instruction
HASWELL_ARCH_NEW = "haswell"
POPCNT_FLAG = "popcnt"
if self.use_old_arch_names(4, 9):
    ret_val = self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
                HASWELL_ARCH_OLD + " "
    exit(ret_val + self.BAZEL_PREFIX_ + self.FLAG_PREFIX_ + \
             POPCNT_FLAG + " ")
else:
    exit(self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
             HASWELL_ARCH_NEW + " ")
