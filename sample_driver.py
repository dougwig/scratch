
import abstract_driver_heirarchy as abs

class SampleDriver(abs.LoadBalancerAbstractDriver):
    def __init__(self):
        self.register_manager('lbaas-lb', LoadBalancerManager)
        self.register_manager('lbaas-listener', ListenerManager)
        self.register_manager('lbaas-pool', PoolManager)
        self.register_manager('lbaas-member', MemberManager)
        self.register_manager('lbaas-hm', HealthMonitorManager)
        self.register_manager('lbaas-stats', StatsManager)
        self.register_manager('lbaas-tls', TlsManager)


class SampleBaseManager(abs.BaseManager):
    def __init__(self):
        self.rest_client = vendor_rest_init()


class LoadBalancerManager(SampleBaseManager):

    def create(self, context, lb_obj):
        self.rest_client.post('/lb', "{'name': '%s'}" % lb_obj.name)

    def update(self, context, lb_obj):
        self.rest_client.put("/lb/%s" % lb_obj.name, 
                             "{'name': '%s'}" % lb_obj.name)
    def delete(self, context, lb_obj):
        self.rest_client.delete("/lb/%s" % lb_obj.name)

# And so on for listener/member/etc...

class TlsManager(SampleBaseManager):

    def create(self, context, listener_obj, barb_id, key, cert):
        self.rest_client.post('/cert', "{'name': '%s'}" % barb_id)

    def update(self, context, listener_obj, barb_id, key, cert):
        self.rest_client.put('/cert', "{'name': '%s'}" % barb_id)

    def delete(self, context, listener_obj, barb_id):
        self.rest_client.delete('/cert', "{'name': '%s'}" % barb_id)

    def get(self, context, listener_obj, barb_id):
        self.rest_client.get('/cert', "{'name': '%s'}" % barb_id)

