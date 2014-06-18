

class MyTlsManager(SampleBaseManager):

    def create(self, context, listener_obj, barb_id, key, cert):
        self.rest_client.post('/cert', "{'name': '%s'}" % barb_id)

    def update(self, context, listener_obj, barb_id, key, cert):
        self.rest_client.put('/cert', "{'name': '%s'}" % barb_id)

    def delete(self, context, listener_obj, barb_id):
        self.rest_client.delete('/cert', "{'name': '%s'}" % barb_id)

    def get(self, context, listener_obj, barb_id):
        self.rest_client.get('/cert', "{'name': '%s'}" % barb_id)


