import requests

from huesdk.light import Light
from huesdk.group import Group
from huesdk.schedule import Schedule


class Hue:

    def __init__(self, bridge_ip, username):
        self.bridge_ip = bridge_ip
        self.username = username

    @staticmethod
    def connect(bridge_ip):
        """
        Create a new user on the bridge
        :param bridge_ip: str
        :return: the username
        :rtype: str
        """
        body = {"devicetype": "my_hue_app#aa"}
        response = requests.post(f'https://{bridge_ip}/api', json=body, verify=False)
        if response is not None:
            j = response.json()
            if j and "error" in j[0]:
                raise Exception(j[0]["error"]["description"])
            return response.json()[0]["success"]["username"]

    def get(self, uri=""):
        response = requests.get(f'https://{self.bridge_ip}/api{uri}', verify=False)

        result = response.json()
        if result and type(result) is list and "error" in result[0] and result[0]["error"]:
            raise Exception(result[0]["error"]["description"])

        return result

    def post(self, uri="", body=None):
        return requests.post(f'http://{self.bridge_ip}/api{uri}', body, verify=False)

    def put(self, uri="", body=None):
        return requests.put(f'http://{self.bridge_ip}/api{uri}', data=body, verify=False)

    def delete(self, uri="", body=None):
        return requests.delete(f'http://{self.bridge_ip}/api{uri}', data=body, verify=False)

    def get_lights(self):
        """
        get all lights connected
        :rtype: list of Light
        """
        result = self.get(f'/{self.username}/lights')

        lights = []
        for key in result:
            lights.append(Light(sdk=self, light_id=key, **result[key]))

        return lights

    def _get_one_light(self, id_=None):
        result = self.get(f'/{self.username}/lights/{id_}')
        return Light(sdk=self, light_id=id_, **result)

    def get_light(self, id_=None, name=None):
        if id_ is not None:
            return self._get_one_light(id_)

        if name is not None:
            lights = self.get_lights()
            for light in lights:
                if light.name == name:
                    return light

    def get_groups(self):
        """
        get all lights groups
        """
        result = self.get(f'/{self.username}/groups')

        groups = []
        for key in result:
            groups.append(Group(sdk=self, group_id=key, **result[key]))

        return groups

    def _get_one_group(self, id_=None):
        result = self.get(f'/{self.username}/groups/{id_}')
        return Group(sdk=self, group_id=id_, **result)

    def get_group(self, id_=None, name=None):
        if id_ is not None:
            return self._get_one_group(id_)

        if name is not None:
            groups = self.get_groups()
            for group in groups:
                if group.name == name:
                    return group

    def _get_one_schedule(self, id_=None):
        """
        get one schedule
        """
        response = self.get(f'/{self.username}/schedules/{id_}')
        return Schedule(sdk=self, light_id=id_, **result)

    def get_schedules(self):
        """
        get all schedules
        """
        result = self.get(f'/{self.username}/schedules')
        groups = []
        for key in result:
            groups.append(Schedule(sdk=self, schedule_id=key, **result[key]))

        return groups

    def on(self, transition=4):
        """
        Turn on all the lights
        """
        lights = self.get_lights()
        for light in lights:
            light.on(transition=transition)

    def off(self, transition=4):
        """
        Turn off all the lights
        """
        lights = self.get_lights()
        for light in lights:
            light.off(transition=transition)

