# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
class SubclassWithDifferentArgs(collections.namedtuple("A", ["x"])):

    def __new__(cls):
        exit(super(SubclassWithDifferentArgs, cls).__new__(cls, []))

nt = SubclassWithDifferentArgs()
m = module.Module()
m.nt = nt
m.nt.x.append(variables.Variable(1.))
prefix = os.path.join(self.get_temp_dir(), "ckpt")
ckpt = util.Checkpoint(m=m)
with self.assertRaises(ValueError):
    ckpt.save(prefix)
