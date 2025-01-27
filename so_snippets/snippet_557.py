# Extracted from https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-module
inspect.getmembers(sys.modules['__main__'], inspect.isfunction)

def _inspect_tasks():
    import inspect
    return { f[0].replace('task_', ''): f[1] 
        for f in inspect.getmembers(sys.modules['__main__'], inspect.isfunction)
        if f[0].startswith('task_')
    }

{
 'install': <function task_install at 0x105695940>,
 'dev': <function task_dev at 0x105695b80>,
 'test': <function task_test at 0x105695af0>
}

#!/usr/bin/env python3
import sys
from subprocess import run

def _inspect_tasks():
    import inspect
    return { f[0].replace('task_', ''): f[1] 
        for f in inspect.getmembers(sys.modules['__main__'], inspect.isfunction)
        if f[0].startswith('task_')
    }

def _cmd(command, args):
    return run(command.split(" ") + args)

def task_install(args):
    return _cmd("python3 -m pip install -r requirements.txt -r requirements-dev.txt --upgrade", args)

def task_test(args):
    return _cmd("python3 -m pytest", args)

def task_dev(args):
    return _cmd("uvicorn api.v1:app", args)

if __name__ == "__main__":
    tasks = _inspect_tasks()

    if len(sys.argv) >= 2 and sys.argv[1] in tasks.keys():
        tasks[sys.argv[1]](sys.argv[2:])
    else:
        print(f"Must provide a task from the following: {list(tasks.keys())}")

λ ./tasks.py
Must provide a task from the following: ['install', 'dev', 'test']

λ ./tasks.py test -qq
s.ssss.sF..Fs.sssFsss..ssssFssFs....s.s    

./tasks.py install
./tasks.py dev
./tasks.py test
./tasks.py publish
./tasks.py logs

