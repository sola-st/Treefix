# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
"""Asserts DTensor is of the particular value."""
if issubclass(
    type(result_dtensor), resource_variable_ops.BaseResourceVariable):
    result_dtensor = result_dtensor.value()
if expected_layout is not None:
    # This, the assertEqual, is a pure proto raw bytes comparison. To make it
    # human-readable, use the `to_string` api for Layout for the dedicated msg
    # field.
    #
    # Futhurmore, as the mesh part is very long and usually identical. Try to
    # cut them as well, to make it easier to read.
    expected_str = expected_layout.to_string()
    got_str = api.fetch_layout(result_dtensor).to_string()
    index_for_mesh = expected_str.find('mesh:')
    if index_for_mesh != -1 and got_str.find(
        expected_str[index_for_mesh:]) != -1:
        # the mesh part is same. cut them so it is more readable.
        expected_str = expected_str[:index_for_mesh]
        got_str = got_str[:got_str.find('mesh:')]

    self.assertEqual(
        api.fetch_layout(result_dtensor),
        expected_layout,
        msg=(
            '=======\nexpected layout is\n  {}\n\nwhile got layout is\n  {}\n'
            .format(expected_str, got_str)
        ),
    )

layout = api.fetch_layout(result_dtensor)
unpacked = [t.numpy() for t in api.unpack(result_dtensor)]

# Check global shape.
self.assertAllEqual(expected_result.shape, result_dtensor.shape)

result_dtensor = numpy_util.to_numpy(result_dtensor)

# Check dtype.
# Note: This check needs be after result_dtensor is converted
# into numpy, due to failure with Numpy version 1.18.5.
self.assertEqual(
    expected_result.dtype, result_dtensor.dtype, result_dtensor
)

# Check value on concatenated result DTensor.
self.assertAllClose(expected_result, result_dtensor, atol=tol, rtol=tol)

# In addition to check the 'concatenated' DTensor, we also check all
# "replicated" parts are same.
#
# The algorithm is simple:
# 1. For a mesh with topology (x,y,z,p), and a DTensor with layout ('',z,x).
# 2. Create some data structures:
#   - create a mapping from device id (called offset below) to mesh
#     location. For the mesh above, loc {x:1,y:2,z:2,p:0} means the device
#     is located at that coordinates in the 4-D mesh.
#   - create a mapping from mesh location to device id.
# 3. Find all replicated mesh dimension names, i.e., 'y' and `p` in the
#     example above.
# 4. Iterate over all unpacked components, translate the offset (device id)
#    to mesh location, called (x',y',z',p').
#   - For `y`, which is replicated dim in the mesh, check all unpacked
#     components at (x',*,z',p') are same as the component at (x',0,z',p').
#   - For `p`, which is also replicated dim in the mesh, check all unpacked
#     components at (x',y',z',*) are same as the component at (x',y',z',0).

def hash_key(loc):
    """Hash key for Python dict."""
    # Python dict is unhashable. Creates a sorted dict and dumps as json str.
    d = collections.OrderedDict(sorted(loc.items(), key=lambda x: x[0]))
    exit(json.dumps(d))

offset_to_mesh_loc_dict = layout.mesh.unravel_index()
mesh_loc_to_offset_dict = {}
for offset, loc in offset_to_mesh_loc_dict.items():
    mesh_loc_to_offset_dict[hash_key(loc)] = offset

# pylint: disable=protected-access
replicated_dims = [
    x for x in layout.mesh._dim_names if x not in layout.sharding_specs
]
# pylint: enable=protected-access

for offset, tensor in enumerate(unpacked):
    mesh_loc = offset_to_mesh_loc_dict[offset]
    for dim_sharding in replicated_dims:
        if mesh_loc[dim_sharding] != 0:
            mesh_loc = copy.deepcopy(mesh_loc)  # deepcopy as we will mutate
            mesh_loc[dim_sharding] = 0
            offset = mesh_loc_to_offset_dict[hash_key(mesh_loc)]
            # tol is be as low as possible as they should match "exactly". so, we
            # ignore the `tol` passed by caller and choose the default one.
            self.assertAllClose(tensor, unpacked[offset])
