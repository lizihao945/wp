import os
import sys
import shutil
import zipfile
import datetime

dest = "/tmp/app"

def exec_shell(cmd):
	#print "$" + cmd
	os.system(cmd)

def extract_apks(path):

	print "...working in " + os.getcwd()

	# remove the folder if exists
	exec_shell("rm -rf " + dest)

	# copy the apks
	exec_shell("cp -r " + path + "/system/app " + dest)
	print "...pre-installed apps copied"

	print "...extracing apks"
	apps = set()

	os.chdir(dest)

	# get all the app names
	for filename in os.listdir("."):
		if filename.endswith(".apk"):
			apps.add(filename[:-4])

	for appname in apps:
		exec_shell("mkdir " + appname)

		# use classes.dex or [appname].odex
		odex = os.getcwd() + "/" + appname + ".odex"
		if os.path.exists(odex):
			print odex.split("/")[-1] + " found"
			exec_shell("mv " + odex + " " + appname)
		else:
			exec_shell("unzip -j " + appname + ".apk classes.dex -d " + appname + " > /tmp/foo")

		# decode the xml file
		exec_shell("/usr/share/androguard/androaxml.py -i " + appname + ".apk -o AndroidManifest.xml")
		exec_shell("mv AndroidManifest.xml " + appname)
		exec_shell("rm -f " + appname + ".apk")
	os.chdir("..")

	str = "/home/james/pre-installed/" + path.split("/")[-1]

	exec_shell("rm -rf " + str)
	exec_shell("mv app " + str)

if __name__ == '__main__':

	start_time = datetime.datetime.now()

	extract_apks("/home/james/firmwares/miui_GalaxyNexus_4.5.9_5797ac9767_4.2")
	#extract_apks("/home/james/firmwares/test")

	end_time = datetime.datetime.now()
	print('The code ran for %ds' % ((end_time - start_time).seconds))