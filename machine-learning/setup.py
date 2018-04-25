#!//usr/bin/python 

import os 
import urllib
import tarfile

class Setup(object):
	def __init__(self):
		print "install pip ..."
		os.system("sudo apt-get install -y python-pip")

		print "update pip ..."
		os.system("sudo pip install --upgrade pip")

	def installModule(self, module):
		# try:
		# 	import module
		
		# except ImportError:
		# 	print "module is not installed!"
		# 	print "Installing it now ..."

		# import module 
		print "\nInstalling " + module + "..."
		os.system("sudo pip install " + module)
		print 

	def downloadDataset(self, link, filename):
		#urllib.urlretrieve(link, filename="../"+filename)
		urllib.urlretrieve(link, filename=filename)
		print "Download Completed!\n"

		print "Unpacking tar file ..."
		#os.chdir("..")

		tar = tarfile.open(filename, "r:gz")
		tar.extractall()
		tar.close()

		os.system("rm "+ filename)

		print "Unpacking Completed!\n"

	def uninstallModule(self, module):
		print "\nUninstalling " + module 
		os.system("sudo pip uninstall -y " + module) 


if __name__ == '__main__':
  s=Setup()
	
  moduleList=["pandas", "numpy", "nltk", "scipy", "scikit-learn", "matplotlib"]

  # uninstall old modules - clean up 
  print "Uninstall old modules\n"
  for j in range(len(moduleList)):
	s.uninstallModule(moduleList[j])

  print "\n\n"
  
  # install mudules 
  for i in range(len(moduleList)):
  	s.installModule(moduleList[i])

  print

  url="https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
  s.downloadDataset(url, "enron_mail_20150507.tar.gz")


