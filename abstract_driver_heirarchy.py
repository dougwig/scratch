
import abc

import six


@six.add_metaclass(abc.ABCMeta)
class LoadBalancerAbstractDriver(object):

    @abc.abstractproperty
    def load_balancer(self):
        pass

    @abc.abstractproperty
    def listener(self):
        pass

    @abc.abstractproperty
    def pool(self):
        pass

    @abc.abstractproperty
    def member(self):
        pass

    @abc.abstractproperty
    def stats(self):
        pass

@six.add_metaclass(abc.ABCMeta)
class BaseManager(object):

    @abc.abstractmethod
    def create(self, context, obj):
        pass

    @abc.abstractmethod
    def update(self, context, obj_old, obj):
        pass

    @abc.abstractmethod
    def delete(self, context, obj):
        pass


# class LoadBalancerManager(BaseManager):
#     # Must have create/update/delete

# class ListenerManager(BaseManager):
#     # Must have create/update/delete

# class PoolManager(BaseManager):
#     # Must have create/update/delete

# class MemberManager(BaseManager):
#     # Must have create/update/delete

# class HealthMonitorManager(BaseManager):
#     # Must have create/update/delete

# class StatsManager(BaseManager):
#     # Must have get

