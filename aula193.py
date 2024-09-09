import subprocess
import sys

cmd  = ['ping',  '127.0.0.1']
encoding = 'utf_8'
system = sys.platform

if system == "win32":
    cmd = ['ping',  '127.0.0.1']
    encoding = 'cp852'

proc = subprocess.run(
    cmd, capture_output=True,
)

print()

# print(proc.args)
# print(proc.stderr)
print(proc.stdout.decode('cp852'))
# print(proc.returncode)