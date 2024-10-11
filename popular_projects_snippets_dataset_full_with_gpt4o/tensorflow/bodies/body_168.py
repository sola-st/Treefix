# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
ICELAKE_ARCH_OLD = "skylake-avx512"
ICELAKE_ARCH_NEW = "icelake-server"
AVX512_FLAGS = ["avx512f", "avx512cd"]
if IntelPlatform.use_old_arch_names(self, 8, 4):
    ret_val = self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
        ICELAKE_ARCH_OLD + " "
    for flag in AVX512_FLAGS:
        ret_val += self.BAZEL_PREFIX_ + self.FLAG_PREFIX_ + flag + " "
    exit(ret_val)
else:
    exit(self.BAZEL_PREFIX_ + self.ARCH_PREFIX_ + \
             ICELAKE_ARCH_NEW + " ")
