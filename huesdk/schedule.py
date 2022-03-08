import json


class Schedule:

    def __init__(self, sdk, schedule_id, **kwargs):
        """
        :param str schedule_id: id of the schedule
        """
        self.sdk = sdk

        self.id_ = schedule_id
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.command = kwargs.get('command', None)
        self.time = kwargs.get('time', None)
        self.created = kwargs.get('created', None)
        self.status = kwargs.get('status', None)
        self.autodelete = kwargs.get('autodelete', None)
        self.starttime = kwargs.get('starttime', None)

    def _put(self, body):
        response = self.sdk.put(uri=f'/{self.sdk.username}/schedules/{self.id_}', body=json.dumps(body))

    def delete(self):
        response = self.sdk.delete(uri=f'/{self.sdk.username}/schedules/{self.id_}')

    def set_name(self, name):
        self._put({"name": name})
        self.name = name

    def set_description(self, description):
        self._put({"description": description})
        self.description = description