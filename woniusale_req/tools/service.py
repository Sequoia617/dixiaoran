# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         service
# Description:  
# Author:       Administrator
# Date:         2020/4/3
#-------------------------------------------------------------------------------

class Service:

	# 提供session的方法
	@classmethod
	def get_session(cls):
		import requests
		return requests.session()

# 通过登录的动作给session添加cookie
	@classmethod
	def set_cookie(cls,session):
		from woniusale_req.tools.util import Utility
		contents = Utility.get_json('..\\conf\\base.conf')
		login_url = f'{contents["PROTOCOL"]}://{contents["HOSTNAME"]}:' \
		            f'{contents["PORT"]}/{contents["PROGRAM"]}{contents["LOGINURL"]}'
		login_data = {'username':contents["USERNAME"],"password":contents["PASSWORD"],
		              "verifycode":contents["VERIFYCODE"]}
		print(login_url)
		print(login_data)
		resp = session.post(login_url,login_data)
		print(resp.text)

if __name__ == '__main__':
	import requests
	session = requests.session()
	Service.set_cookie(session)