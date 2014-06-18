
import abstract_driver_heirarchy as abs
import my_tls_handler

class SampleDriver(abs.LoadBalancerAbstractDriver):
    def __init__(self):
        self.set_required_handlers(MyLoadBalancerManager, MyListenerManager,
                                   MyPoolManager, MyMemberManager,
                                   MyHealthMonitorManager, MyStatsManager)
        self.register_optional_handler('lbaas-tls', my_tls_handler.TlsManager)


class SampleBaseManager(abs.BaseManager):
    def __init__(self):
        self.rest_client = vendor_rest_init()


class MyLoadBalancerManager(SampleBaseManager):

    def create(self, context, lb_obj):
        self.rest_client.post('/lb', "{'name': '%s'}" % lb_obj.name)

    def update(self, context, lb_obj):
        self.rest_client.put("/lb/%s" % lb_obj.name, 
                             "{'name': '%s'}" % lb_obj.name)
    def delete(self, context, lb_obj):
        self.rest_client.delete("/lb/%s" % lb_obj.name)

# And so on for listener/member/etc...
