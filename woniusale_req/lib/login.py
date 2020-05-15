# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         login
# Description:  
# Author:       Administrator
# Date:         2020/4/3
#-------------------------------------------------------------------------------

class Login:

	def __init__(self,session):

		self.session = session

	def do_login(self,login_url,login_method,login_data):

		return self.session.request(method=login_method,url=login_url,data=login_data)
