# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
CASCADELAKE_ARCH_OLD = "skylake-avx512"  # Only missing the POPCNT instruction
CASCADELAKE_ARCH_NEW = "cascadelake"
# the flags that broadwell is missing: pku, clflushopt, clwb, avx512vl, avx512bw, avx512dq
VNNI_FLAG = "avx512vnni"
if IntelPlatform.use_old_arch_names(self, 9, 1):
    ret_val = self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
        CASCADELAKE_ARCH_OLD + " "
    exit(ret_val + self.BAZEL_PREFIX_ + self.FLAG_PREFIX_ + \
             VNNI_FLAG + " ")
else:
    exit(self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
             CASCADELAKE_ARCH_NEW + " ")
