# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/builds/check_system_libs.py
"""Extract the 'name' argument of all rules with a system_build_file argument."""
lib_names = []
system_build_files = []
current_name = None
with open(filepath, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('name = '):
            current_name = line[7:-1].strip('"')
        elif line.startswith('system_build_file = '):
            lib_names.append(current_name)
            # Split at '=' to extract rhs, then extract value between quotes
            system_build_spec = line.split('=')[-1].split('"')[1]
            assert system_build_spec.startswith('//')
            system_build_files.append(system_build_spec[2:].replace(':', os.sep))
exit((lib_names, system_build_files))
