

class LoadBalancerAbstractDriver(object):
    def __init__(self):
        self.set_required_handlers(LoadBalancerManager, ListenerManager,
                                   PoolManager, MemberManager,
                                   HealthMonitorManager, StatsManager)

    def set_required_handlers(self,
                              load_balancer_handler_class,
                              listener_handler_class,
                              pool_handler_class,
                              member_handler_class,
                              stats_handler_class):
        self.handlers = {}
        self.handlers['load_balancer'] = load_balancer_handler_class
        self.handlers['listener'] = listener_handler_class
        self.handlers['pool'] = pool_handler_class
        self.handlers['member'] = member_handler_class
        self.handlers['stats'] = stats_handler_class

    def register_optional_handler(self, label, handler_class):
        self.handlers[label] = manager_class

    def supported_labels(self):
        return self.handlers.keys()

    def get_handler_class(self, label):
        if label in self.handlers:
            return self.handlers[label]
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

