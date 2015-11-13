import os, sys
tasks_path = os.path.realpath(os.path.join(os.path.realpath(__file__), '..', '..'))
sys.path.insert(0, tasks_path)
from tasks.operation import add

result = add.delay(2, 3)
print result.get()

exit(0)
