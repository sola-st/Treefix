# Extracted from https://stackoverflow.com/questions/30216000/why-is-faster-than-list
Python 2.7.3
import dis
dis.dis(lambda: list())
  1           0 LOAD_GLOBAL              0 (list)
              3 CALL_FUNCTION            0
              6 RETURN_VALUE        
dis.dis(lambda: [])
  1           0 BUILD_LIST               0
              3 RETURN_VALUE        

