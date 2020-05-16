# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         startup
# Description:  
# Author:       Administrator
# Date:         2020/3/25
#-------------------------------------------------------------------------------
import unittest
from HTMLTestRunner import HTMLTestRunner

from tools.util import Utility


class Startup:

	# 启动测试
	@classmethod
	def start(cls):
		suite = unittest.TestSuite()
		loader = unittest.TestLoader()
		names = Utility.trans_str('..\\conf\\test.conf')
		print(names)
		tests = loader.loadTestsFromNames(names)
		suite.addTests(tests)
		with open('..\\report\\%s_report.html'%(Utility.get_ctime()),'w') as file:
			runner = HTMLTestRunner(stream=file,verbosity=2)
			runner.run(suite)

if __name__ == '__main__':
	Startup.start()