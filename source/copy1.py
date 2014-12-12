import os;
import sys;
import string;
import glob;
import shutil;


if __name__ == "__main__" :
	print glob.glob(r'./*.txt')

	filname = "/Users/zhiweiliu/learn/python_learn/copy_test/source/*.*"
	print filname
	olFileToCopy = glob.glob(filname)
	print olFileToCopy
	print str(len(olFileToCopy))
	sys.exit(0)