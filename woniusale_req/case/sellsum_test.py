

import unittest,warnings
from parameterized import parameterized
from woniusale_req.tools.util import Utility

class SellsumTest(unittest.TestCase):
    add_sellsum_conf = Utility.get_json('..\\conf\\testinfo.conf')[4]
    add_sellsum_info = Utility.trans_tuple(add_sellsum_conf)
    query_sellsum_conf = Utility.get_json('..\\conf\\testinfo.conf')[5]
    query_sellsum_info = Utility.trans_tuple(query_sellsum_conf)
    sell_sellsum_conf = Utility.get_json('..\\conf\\testinfo.conf')[6]
    sell_sellsum_info = Utility.trans_tuple(sell_sellsum_conf)
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        from woniusale_req.lib.sellsum import Sellsum
        from woniusale_req.tools.service import Service
        self.min = Sellsum(Service.get_session())


    def tearDown(self):
        pass

    @parameterized.expand(add_sellsum_info)
    def test_add_sellsum(self,url, method, bcode, expect):
        add_sellsum_data = {'URL':url,'METHOD':method,
		                    "ADDMINUTESDATA":{"barcode":bcode},
		                    'EXPECT':expect}
        add_sellsum_resp = self.min.do_add_sellsum(add_sellsum_data['URL'],add_sellsum_data['METHOD'],add_sellsum_data['ADDMINUTESDATA'])
        result = add_sellsum_resp.json()
        result1 = add_sellsum_resp.text
        print(result1)
        if result == []:
            actual = 'add faild'
        elif 'barcode' in result[0]:
                actual = 'add success'
        self.assertEqual(actual,add_sellsum_data['EXPECT'])

    @parameterized.expand(query_sellsum_info)
    def test_query_sellsum(self,url, method, cphone, expect):
        query_sellsum_data = {'URL':url,'METHOD':method,
		                    "ADDMINUTESDATA":{"customerphone":cphone},
		                    'EXPECT':expect}
        query_sellsum_resp = self.min.do_query_sellsum(query_sellsum_data['URL'],query_sellsum_data['METHOD'],query_sellsum_data['ADDMINUTESDATA'])
        result = query_sellsum_resp.json()
        if result == []:
            acutal = 'query faild'
        else:
            if 'childsex' in result[0]:
                acutal = 'query success'

        self.assertEqual(acutal,query_sellsum_data['EXPECT'])

    @parameterized.expand(sell_sellsum_info)
    def test_sell_sellsum(self,url, method,cphone,paythod,total,ratio,csum,ttype,tsum,old,expect):
        sell_sellsum_data = {'URL':url,'METHOD':method,
		                    "ADDMINUTESDATA":{"customerphone":cphone,"paymethod":paythod,"totalprice":total,"creditratio":ratio,"creditsum":csum,"tickettype":ttype,"ticketsum":tsum,"oldcredit":old},
		                    'EXPECT':expect}
        sql = 'select sellsumid from sellsum order by sellsumid desc'
        result1 = Utility.query_one(sql)
        sell_sellsum_resp = self.min.do_sell_sellsum(sell_sellsum_data['URL'],sell_sellsum_data['METHOD'],sell_sellsum_data['ADDMINUTESDATA'])
        result = sell_sellsum_resp.text
        print(result)
        if 'Error' in result:
            acutal = 'sell faild'
        else:
            if int(result1[0]) + 1 == int(result):
                acutal = 'sell success'
            else:
                acutal = 'sell failed'
        self.assertEqual(acutal,sell_sellsum_data['EXPECT'])

if __name__ == '__main__':

    unittest.main(verbosity=2)
