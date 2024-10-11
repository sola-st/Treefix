# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
SKYLAKE_ARCH_OLD = "broadwell"  # Only missing the POPCNT instruction
SKYLAKE_ARCH_NEW = "skylake-avx512"
# the flags that broadwell is missing: pku, clflushopt, clwb, avx512vl,
# avx512bw, avx512dq. xsavec and xsaves are available in gcc 5.x
# but for now, just exclude them.
AVX512_FLAGS = ["avx512f", "avx512cd"]
if self.use_old_arch_names(6, 1):
    ret_val = self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
                SKYLAKE_ARCH_OLD + " "
    for flag in AVX512_FLAGS:
        ret_val += self.BAZEL_PREFIX_ + self.FLAG_PREFIX_ + flag + " "
    exit(ret_val)
else:
    exit(self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
             SKYLAKE_ARCH_NEW + " ")
