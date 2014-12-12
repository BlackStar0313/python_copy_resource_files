# -*- coding: utf-8 -*-
import os;
import sys;
import string;
import glob;    #文件操作相关
import shutil; 	#实现文件的复制删除

def CopyFile(strSourceFileName,strDirectionFileName) :

	strRealRootDir = os.path.realpath(strSourceFileName)   #获取脚本(文件)所在目录
	print "realpath is :" + strRealRootDir
	if (os.path.isdir(strRealRootDir) == True ) :	 #判断相关路径是否是目录
		print "it's a realpath~~~~~ "

	filename = strRealRootDir + "/" + "*.txt";
	#strLine = string.replace(filename,"/","\\")

	olFileToCopy = glob.glob(filename)				#获取文件名字对应的路径。保存在一个数组中
	loopCount = 0
	while loopCount < len(olFileToCopy):
		outFile = olFileToCopy[loopCount]
		loopCount += 1
		print outFile
		#if (os.path.isfile(outFile) == True):
		#	print "it's a real filename~~~~~~~~"
		#	ofFile = open(outFile)
		#	strRead = ofFile.readline();
		#	print strRead 
		strCopyName = os.path.basename(outFile)		#取得主文件名
		# strDirection = os.path.realpath("direction")  #目标文件路径
		strDirection = os.path.realpath(strDirectionFileName)  #目标文件路径
		strDirection = strDirection + "/" + strCopyName
		print strDirection
		#if (os.path.isdir(strDirection) == False):
		#	print "it's not a dir"
		shutil.copyfile(outFile,strDirection)		#拷贝文件到目的目录


if __name__ == "__main__":
	print "hello world!!"
	syslength = len(sys.argv)
	print "sys lenght is :" + str(syslength)

	count = 0;
	# while (count < syslength) :
	# 	print "sys argv 1 is :" + sys.argv[count];
	# 	count += 1

	# for i in range(0,syslength) :
	# 	print "sys argv 1 is :" + sys.argv[i];
	if syslength < 3:
		print "Are you fucking killing me ! man!!! you are to short~ please input the right commond like this : python copy.py <strSourceFileName> <strDirectionFileName>"
	else :
		CopyFile(sys.argv[1] , sys.argv[2])


	sys.exit(0)


