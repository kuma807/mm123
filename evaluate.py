import subprocess
import time
sum = 0
for i in range(50):
    start = time.time()
    res = str(subprocess.check_output(['./run.sh', str(i)]))
    res = res[10:]
    res = res.replace('\\n', '').replace('\'', '')
    sum += float(res)
    end = time.time()
    print(end - start)
print(sum)
