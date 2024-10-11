# Extracted from https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
class base(object):
    def __init__(self, base_param):
        self.base_param = base_param


class child1(base): # inherited from base class
    def __init__(self, child_param, *args) # *args for non-keyword args
        self.child_param = child_param
        super(child1, self).__init__(*args) # call __init__ of the base class and initialize it with a NON-KEYWORD arg

class child2(base):
    def __init__(self, child_param, **kwargs):
        self.child_param = child_param
        super(child2, self).__init__(**kwargs) # call __init__ of the base class and initialize it with a KEYWORD arg

c1 = child1(1,0)
c2 = child2(1,base_param=0)
print c1.base_param # 0
print c1.child_param # 1
print c2.base_param # 0
print c2.child_param # 1

