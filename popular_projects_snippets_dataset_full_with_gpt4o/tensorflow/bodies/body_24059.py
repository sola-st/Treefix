# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
super().__init__()
self.z = MemberType()
self.a = container_type([MemberType(), MemberType()])
if create_child:
    self.c = SimpleModule(create_child=False)
