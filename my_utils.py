import os
import shutil
import zipfile
import datetime

def exec_shell(cmd):
	#print "$" + cmd
	os.system(cmd)

def extract_apks(path):
	dest = "/home/james/pre-installed"

	start_time = datetime.datetime.now()

	print "...working in " + os.getcwd()
	print

	# remove the folder if exists
	exec_shell("rm -rf " + dest)

	# copy the apks
	exec_shell("cp -r " + path + "/system/app .")
	exec_shell("mv app " + dest)
	print "...pre-installed apps copied"
	print

	print "...extracing apks"
	os.chdir(dest)
	for filename in os.listdir("."):
		if filename.endswith(".apk"):
			exec_shell("unzip " + filename + " -d " + filename[:-4])
	os.chdir("..")

	end_time = datetime.datetime.now()
	print('The code ran for %ds' % ((end_time - start_time).seconds))

if __name__ == '__main__':
	extract_apks("/home/james/firmwares/miui_GalaxyNexus_4.5.9_5797ac9767_4.2")