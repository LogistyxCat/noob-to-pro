


import optparse
import zipfile
from threading import Thread

def extract_zip(zfile, password):
	try:
		zfile.extractall(pwd=password)
		print "[+] Password Found: " + password + '\n'
	except:
		pass

def main():
	parser = optparse.OptionParser("-f <zipfile> -w <word_list>")
	parser.add_option('-f', dest='zname', type='string',help='specify zip file')
	parser.add_option('-w', dest='wname', type='string',help='specify word  list file')
	(options, arg) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname

	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)

	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extract_zip, args=(zFile, password))
		t.start()

if __name__ == '__main__':
	main()


