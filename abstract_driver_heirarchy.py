

class LoadBalancerAbstractDriver(object):
    LBAAS_REQUIRED_MANAGERS = {
        'lbaas-lb': LoadBalancerManager,
        'lbaas-listener': ListenerManager,
        'lbaas-pool': PoolManager,
        'lbaas-member': MemberManager,
        'lbaas-hm': HealthMonitorManager,
        'lbaas-stats': StatsManager
    }

    def __init__(self):
        self.managers = {}
        for k,v in LBAAS_REQUIRED_MANAGERS.items():
            self.managers[k] = v

    def register_manager(self, label, manager_class):
        self.managers[label] = manager_class

    def supported_labels(self):
        return self.managers.keys()

    def get_manager_class(self, label):
        if label in self.managers:
            return self.managers[label]
        return None


class BaseManager(object):

    def create(self, context, obj):
        raise ex.NotImplemented()

    def update(self, context, obj_old, obj):
        raise ex.NotImplemented()

    def delete(self, context, obj):
        raise ex.NotImplemented()

    def get(self, context, obj):
        # Optional
        return None


class LoadBalancerManager(BaseManager):
    # Must have create/update/delete

class ListenerManager(BaseManager):
    # Must have create/update/delete

class PoolManager(BaseManager):
    # Must have create/update/delete

class MemberManager(BaseManager):
    # Must have create/update/delete

class HealthMonitorManager(BaseManager):
    # Must have create/update/delete

class StatsManager(BaseManager):
    # Must have get

