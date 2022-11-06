import time
#Finding the Seconds epoch
seconds=time.time()
print("Seconds since epoch=",seconds)
local_time=time.ctime(seconds)
print("Local time :", local_time)
