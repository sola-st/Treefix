# Extracted from ./data/repos/tensorflow/tensorflow/cc/saved_model/testdata/generate_saved_models.py
if len(args) != 3:
    print("Expected: {export_path} {ModuleName}")
    print("Allowed ModuleNames:", MODULE_CTORS.keys())
    exit(1)

_, export_path, module_name = args
module_ctor, version = MODULE_CTORS.get(module_name)
if not module_ctor:
    print("Expected ModuleName to be one of:", MODULE_CTORS.keys())
    exit(2)
os.makedirs(export_path)

tf_module = module_ctor()
if version == 2:
    options = save_options.SaveOptions(save_debug_info=True)
    saved_model.save(tf_module, export_path, options=options)
else:
    builder = saved_model.builder.SavedModelBuilder(export_path)
    builder.add_meta_graph_and_variables(tf_module, ["serve"])
    builder.save()
