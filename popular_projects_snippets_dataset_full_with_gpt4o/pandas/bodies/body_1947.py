# Extracted from ./data/repos/pandas/pandas/tests/api/test_api.py

checkthese = (
    self.public_lib
    + self.private_lib
    + self.misc
    + self.modules
    + self.classes
    + self.funcs
    + self.funcs_option
    + self.funcs_read
    + self.funcs_json
    + self.funcs_to
    + self.private_modules
)
self.check(namespace=pd, expected=checkthese, ignored=self.ignored)
