

class Sellsum:

    def __init__(self,session):

        self.session = session
        from woniusale_req.tools.service import Service
        Service.set_cookie(self.session)


    def do_add_sellsum(self,add_sellsum_url,add_sellsum_method,add_sellsum_data):
        return self.session.request(url=add_sellsum_url, method=add_sellsum_method, data=add_sellsum_data)

    def do_query_sellsum(self,query_sellsum_url,query_sellsum_method,query_sellsum_data):
        return self.session.request(url=query_sellsum_url, method=query_sellsum_method, data=query_sellsum_data)

    def do_sell_sellsum(self,sell_sellsum_url,sell_sellsum_method,sell_sellsum_data):
        return self.session.request(url=sell_sellsum_url, method=sell_sellsum_method, data=sell_sellsum_data)

    # def do_delete_minutes(self,delete_minutes_url,delete_minutes_method,delete_minutes_data):
    #     return self.session.request(url=delete_minutes_url, method=delete_minutes_method, data=delete_minutes_data)



