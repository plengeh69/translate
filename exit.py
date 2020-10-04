import os,sys,time


def l(z):
    for e in z + "\n":
	sys.stdout.write(e)
	sys.stdout.flush()
	time.sleep(0.05)

l("\n \033[1;95mThanks To Use This Tools \033[1;96m:\033[1;93m)")
time.sleep(1)
l(" \033[1;95mCoding By \033[4;96mPaijoasu!\033[1;0m")
time.sleep(1)
os.system("clear")
exit()