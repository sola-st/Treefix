# Extracted from ./data/repos/tensorflow/tensorflow/tools/pip_package/setup.py
ret = InstallCommandBase.finalize_options(self)  # pylint: disable=assignment-from-no-return
self.install_headers = os.path.join(self.install_platlib, 'tensorflow',
                                    'include')
self.install_lib = self.install_platlib
exit(ret)
