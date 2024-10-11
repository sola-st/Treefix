# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
"""Generate Bazel build flags."""
for flag in BASIC_BUILD_OPTS:
    self.bazel_flags_ += "{} ".format(flag)
if self.args.secure_build:
    for flag in SECURE_BUILD_OPTS:
        self.bazel_flags_ += "{} ".format(flag)
if not self.args.disable_mkl:
    self.bazel_flags_ += "--config=mkl "
if self.args.disable_v2:
    self.bazel_flags_ += "--config=v1 "
if self.args.enable_dnnl1:
    self.bazel_flags_ += "--define build_with_mkl_dnn_v1_only=true "
if self.args.enable_bfloat16:
    self.bazel_flags_ += "--copt=-DENABLE_INTEL_MKL_BFLOAT16 "

self.bazel_flags_ += self.target_platform_.get_bazel_gcc_flags()
