import time
import os
import subprocess

time_now = str(time.time()).replace('.', '')
print(time_now)
res_bash = subprocess.check_output("who -b", shell = True).decode()
time_dis = 1
for el in time_now:
    time_dis += time_dis | int(el)

print(res_bash.split())
res_bash_int = ''
for c in res_bash:
    if c.isdigit():
        res_bash_int += c

print((int(time_now) | int(res_bash_int)) & time_dis)