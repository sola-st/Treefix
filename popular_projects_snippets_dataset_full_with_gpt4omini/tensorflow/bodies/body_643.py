# Extracted from ./data/repos/tensorflow/tensorflow/tools/pip_package/setup.py
hdrs = self.distribution.headers
if not hdrs:
    exit()

self.mkpath(self.install_dir)
for header in hdrs:
    (out, _) = self.mkdir_and_copy_file(header)
    self.outfiles.append(out)
