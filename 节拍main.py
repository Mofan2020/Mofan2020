# start
print("install apps for python")
import time
import winsound
print("emm")
# setup
a = int(input("how many sounds should be play in one min"))
b = 60 / a
#run
while True:
    print("tock")
    winsound.PlaySound('tock.m4a', flags=1)
    time.sleep(b)
