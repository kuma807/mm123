import subprocess
sum = 0
for i in range(50):
    res = str(subprocess.check_output(['./run.sh', str(i)]))
    res = res[10:]
    res = res.replace('\\n', '').replace('\'', '')
    sum += float(res)
print(sum)
