# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         login_test
# Description:  
# Author:       Administrator
# Date:         2020/4/3
#-------------------------------------------------------------------------------

import unittest,warnings
from parameterized import parameterized


from woniusale_req.tools.util import Utility


class LoginTest(unittest.TestCase):

	login_conf = Utility.get_json('..\\conf\\testinfo.conf')[0]
	login_info = Utility.trans_tuple(login_conf)
	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		from woniusale_req.lib.login import Login
		from woniusale_req.tools.service import Service
		self.login = Login(Service.get_session())

	def tearDown(self):
		pass

	@parameterized.expand(login_info)
	def test_login(self,url,method,uname,upass,vcode,expect):
		warnings.simplefilter('ignore',ResourceWarning)
		login_test_info = {'URL':url,'METHOD':method,
		                   'LOGINDATA':{'username':uname,'password':upass,'verifycode':vcode},'EXPECT':expect}
		login_resp = self.login.do_login(login_test_info['URL'],login_test_info['METHOD'],login_test_info['LOGINDATA'])
		result = login_resp.text
		if result == 'login-pass':
			actual = 'login-pass'
		elif result == 'login-fail':
			actual = 'login-fail'
		else:
			actual = 'vcode-error'
		self.assertEqual(actual,login_test_info['EXPECT'])

if __name__ == '__main__':
	unittest.main(verbosity=2)