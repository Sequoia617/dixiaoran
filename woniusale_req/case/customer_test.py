import unittest, warnings
from parameterized import parameterized
from woniusale_req.tools.util import Utility


class CustomerTest(unittest.TestCase):
    add_customer_conf = Utility.get_json('..\\conf\\testinfo.conf')[1]
    add_customer_info = Utility.trans_tuple(add_customer_conf)
    query_customer_conf = Utility.get_json('..\\conf\\testinfo.conf')[2]
    query_customer_info = Utility.trans_tuple(query_customer_conf)
    edit_customer_conf = Utility.get_json('..\\conf\\testinfo.conf')[3]
    edit_customer_info = Utility.trans_tuple(edit_customer_conf)

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        from woniusale_req.lib.customer import Customer
        from woniusale_req.tools.service import Service
        self.min = Customer(Service.get_session())

    def tearDown(self):
        pass

    @parameterized.expand(add_customer_info)
    def test_add_customer(self, url, method, cname, cphone, csex, cdate,
                          ckids, ccloth, expect):
        add_customer_data = {'URL': url, 'METHOD': method,
                             "ADDMINUTESDATA": {"customername": cname, "customerphone": cphone, "childsex": csex
                                 , "childdate": cdate, "creditkids": ckids, "creditcloth": ccloth},
                             'EXPECT': expect}
        add_customer_resp = self.min.do_add_customer(add_customer_data['URL'], add_customer_data['METHOD']
                                                     , add_customer_data['ADDMINUTESDATA'])
        result = add_customer_resp.text
        print(result)
        if result == 'add-successful':
            actual = 'add success'
        elif result == 'already-added':
            actual = 'already-added'
        elif 'Error' in result:
            actual = 'error'
        self.assertEqual(actual, add_customer_data['EXPECT'])

    @parameterized.expand(query_customer_info)
    def test_query_customer(self, url, method, cphone, pag, expect):
        query_customer_data = {'URL': url, 'METHOD': method,
                               "ADDMINUTESDATA": {"customerphone": cphone, "page": pag},
                               'EXPECT': expect}
        query_customer_resp = self.min.do_query_customer(query_customer_data['URL'], query_customer_data['METHOD']
                                                         , query_customer_data['ADDMINUTESDATA'])
        result = query_customer_resp.json()
        result1 = query_customer_resp.text
        print(result1)
        if result == []:
            acutal = 'query faild'
        else:
            if 'childsex' in result[0]:
                acutal = 'query success'

        self.assertEqual(acutal, query_customer_data['EXPECT'])

    @parameterized.expand(edit_customer_info)
    def test_edit_customer(self, url, method, cid, cname, cphone, csex, cdate,
                           ckids, ccloth, expect):
        edit_customer_data = {'URL': url, 'METHOD': method,
                              "ADDMINUTESDATA": {"customerid": cid, "customerphone": cphone, "customername": cname
                                  , "childsex": csex, "childdate": cdate, "creditkids": ckids
                                  , "creditcloth": ccloth},
                              'EXPECT': expect}
        edit_customer_resp = self.min.do_edit_customer(edit_customer_data['URL'], edit_customer_data['METHOD']
                                                       , edit_customer_data['ADDMINUTESDATA'])
        result = edit_customer_resp.text
        print(result)
        if result == 'edit-successful':
            actual = 'edit success'
        elif 'Error' in result:
            actual = 'edit faild'
        self.assertEqual(actual, edit_customer_data['EXPECT'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
