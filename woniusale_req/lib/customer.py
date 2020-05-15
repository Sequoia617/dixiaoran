

class Customer:

    def __init__(self,session):

        self.session = session
        from woniusale_req.tools.service import Service
        Service.set_cookie(self.session)


    def do_add_customer(self,add_customer_url,add_customer_method,add_customer_data):
        return self.session.request(url=add_customer_url, method=add_customer_method, data=add_customer_data)

    def do_query_customer(self,query_customer_url,query_customer_method,query_customer_data):
        return self.session.request(url=query_customer_url, method=query_customer_method, data=query_customer_data)

    def do_edit_customer(self,edit_customer_url,edit_customer_method,edit_customer_data):
        return self.session.request(url=edit_customer_url, method=edit_customer_method, data=edit_customer_data)

    # def do_delete_minutes(self,delete_minutes_url,delete_minutes_method,delete_minutes_data):
    #     return self.session.request(url=delete_minutes_url, method=delete_minutes_method, data=delete_minutes_data)



