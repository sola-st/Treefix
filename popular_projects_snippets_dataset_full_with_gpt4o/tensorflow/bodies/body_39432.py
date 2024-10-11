# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/testdata/generate_checkpoint.py
if len(args) != 3:
    print("Expected: {export_path} {ModuleName}")
    print("Allowed ModuleNames:", MODULE_CTORS.keys())
    exit(1)

_, export_path, module_name = args
module_ctor = MODULE_CTORS.get(module_name)
if not module_ctor:
    print("Expected ModuleName to be one of:", MODULE_CTORS.keys())
    exit(2)

tf_module = module_ctor()
ckpt = checkpoint.Checkpoint(tf_module)
ckpt.write(export_path)
