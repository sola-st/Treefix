# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
self.parse_args()
self.target_platform_ = self.PLATFORMS_.get(self.args.target_platform)
if self.validate_args():
    self.set_build_args()
    self.write_build_args()
else:
    print("Error.")
