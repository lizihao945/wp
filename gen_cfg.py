from androguard import *
from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm
from androguard.core.analysis.analysis import VMAnalysis

if __name__ == '__main__':
	path = "crackme02.apk"
	a = apk.APK(path)
	d = dvm.DalvikVMFormat(a.get_dex())
	x = VMAnalysis(d)

	for method in d.get_methods():
		g = x.get_method(method)

		if method.get_code() == None:
			continue

		print method.get_class_name(), method.get_name(), method.get_descriptor()

		idx = 0
		for i in g.get_basic_blocks().get():
			print "\t %s %x %x" % (i.name, i.start, i.end), '[ NEXT = ', ', '.join( "%x-%x-%s" % (j[0], j[1], j[2].get_name()) for j in i.get_next() ), ']', '[ PREV = ', ', '.join( j[2].get_name() for j in i.get_prev() ), ']'
			for ins in i.get_instructions():
				print "\t\t %x" % idx, ins.get_name(), ins.get_output()
			idx += ins.get_length()

		print ""