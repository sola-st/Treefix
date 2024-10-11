# Extracted from https://stackoverflow.com/questions/1483429/how-do-i-print-an-exception-in-python
except Exception as e:
    print(e)

except Exception as e:
    print(e, file=sys.stderr)

