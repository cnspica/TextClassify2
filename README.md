英文分词，采用nltk工具包进行分词
	sudo apt-get install python-nltk
	进入python命令行输入
	>>>import nltk
	>>>nltk.download()
中文分词，采用jieba工具包进行分词


Ubuntu下pil numpy scipy matplotlib的安装：
	sudo apt-get update
	sudo apt-get install git g++
	sudo apt-get install python-dev python-setuptools
	
	sudo easy_install Cython 
	sudo easy_install pil
	sudo apt-get install libatlas-base-dev # 科学计算库
	sudo apt-get install gfortran # fortran编译器
	sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev
	export BLAS=/usr/lib/libblas/libblas.so 
	export LAPACK=/usr/lib/lapack/liblapack.so 
	export ATLAS=/usr/lib/atlas-base/libatlas.so
	sudo apt-get install python-numpy
	sudo apt-get install python-scipy
	sudo apt-get install python-matplotlib
	
	sudo easy_install jieba
	sudo easy_install scikit-learn
	sudo easy_install simplejson
	sudo easy_install pymongo

	
CentOS下pil numpy scipy matplotlib的安装：
	离线安装Python
	sudo yum install python-setuptools
	sudo yum install gcc-gfortran 
	sudo yum install blas-devel
	sudo yum install lapack-devel
	进入numpy解压目录
	sudo python setup.py build
	sudo python setup.py install
	进入scipy解压目录
	sudo python setup.py build
	sudo python setup.py install
	进入matplotlib目录
	sudo yum install libpng-devel
	sudo python setup.py build
	sudo python setup.py install

	sudo easy_install jieba
	sudo easy_install scikit-learn
	sudo easy_install simplejson
	sudo easy_install pymongo
