import os
import shutil
import zipfile
import datetime

dest = "/tmp/app"

def exec_shell(cmd):
	#print "$" + cmd
	os.system(cmd)

def extract_apks(path):

	print "...working in " + os.getcwd()
	print

	# remove the folder if exists
	exec_shell("rm -rf " + dest)

	# copy the apks
	exec_shell("cp -r " + path + "/system/app " + dest)
	print "...pre-installed apps copied"
	print

	print "...extracing apks"
	os.chdir(dest)
	for filename in os.listdir("."):
		if filename.endswith(".apk"):
			exec_shell("unzip " + filename + " -d " + filename[:-4])

	apps = set()
	for foldername in os.listdir("."):
		if os.path.isdir(foldername):
			apps.add(foldername)
	for appname in apps:
		exec_shell("rm -rf " + appname + ".apk")
		exec_shell("mv " + appname + ".odex " + appname)

	os.chdir("..")

	str = "/home/james/pre-installed/" + path.split("/")[-1]

	exec_shell("rm -rf " + str)
	exec_shell("mv -f app " + str)

if __name__ == '__main__':
	start_time = datetime.datetime.now()

	extract_apks("/home/james/firmwares/miui_GalaxyNexus_4.5.9_5797ac9767_4.2")
	#extract_apks("/home/james/firmwares/test")

	end_time = datetime.datetime.now()
	print('The code ran for %ds' % ((end_time - start_time).seconds))