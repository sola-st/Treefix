# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves all Instruction Set Architecture(ISA) available.

  Required ISA(s): 'avx', 'avx2', 'avx512f', 'sse4', 'sse4_1'

  Returns:
    Tuple
      (list of available ISA, list of missing ISA)
  """
key = "cpu_isa"
out, err = run_shell_cmd(cmds_all[PLATFORM.lower()][key])
if err and FLAGS.debug:
    print("Error in detecting supported ISA:\n %s" % str(err))

ret_val = out
required_isa = ["avx", "avx2", "avx512f", "sse4", "sse4_1"]
found = []
missing = []
for isa in required_isa:
    for sys_isa in ret_val.split(b" "):
        if isa == sys_isa:
            if isa not in found:
                found.append(isa)

missing = list(set(required_isa) - set(found))
exit((found, missing))
