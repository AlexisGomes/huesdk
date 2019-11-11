import requests
import json


class Group:

    sdk = None
    username = None

    id_ = None
    name = None

    def __init__(self, sdk, group_id, **kwargs):

        self.sdk = sdk
        self.id_ = group_id

        self.name = kwargs.get('name', None)

        if 'action' in kwargs:
            self.is_on = kwargs['action'].get('on', False)
            self.bri = kwargs['action'].get('bri', None)
            self.hue = kwargs['action'].get('hue', None)
            self.sat = kwargs['action'].get('sat', None)

    def _put(self, body):
        response = self.sdk.put(uri=f'/{self.sdk.username}/groups/{self.id_}', body=json.dumps(body))

    def _put_action(self, body):
        response = self.sdk.put(uri=f'/{self.sdk.username}/groups/{self.id_}/action', body=json.dumps(body))

    def on(self):
        if self.is_on is False:
            self._put_action({"on": True})
            self.is_on = True

    def off(self):
        if self.is_on is True:
            self._put_action({"on": False})
            self.is_on = False

    def set_brightness(self, value):
        self._put_action({"bri": value})

    def set_color(self, value):
        self._put_action({"hue": value})

    def red(self):
        self.set_color(65535)

    def blue(self):
        self.set_color(43690)

    def green(self):
        self.set_color(21845)

    def set_name(self, name):
        self._put({"name": name})
        self.name = name


class Light:

    sdk = None
    username = None

    id_ = None
    name = None
    bri = None
    is_on = False
    hue = None
    sat = None

    def __init__(self, sdk, light_id, **kwargs):
        """
        :param str light_id: id of the light
        """
        self.sdk = sdk

        self.id_ = light_id
        self.name = kwargs.get('name', None)

        if 'state' in kwargs:
            self.is_on = kwargs['state'].get('on', False)
            self.bri = kwargs['state'].get('bri', None)
            self.hue = kwargs['state'].get('hue', None)
            self.sat = kwargs['state'].get('sat', None)

    def _put(self, body):
        response = self.sdk.put(uri=f'/{self.sdk.username}/lights/{self.id_}', body=json.dumps(body))

    def _put_state(self, body):
        response = self.sdk.put(uri=f'/{self.sdk.username}/lights/{self.id_}/state', body=json.dumps(body))

    def on(self):
        if self.is_on is False:
            self._put_state({"on": True})
            self.is_on = True

    def off(self):
        if self.is_on is True:
            self._put_state({"on": False})
            self.is_on = False

    def set_brightness(self, value):
        self._put_state({"bri": value})

    def set_color(self, value):
        self._put_state({"hue": value})

    def red(self):
        self.set_color(65535)

    def blue(self):
        self.set_color(43690)

    def green(self):
        self.set_color(21845)

    def set_name(self, name):
        self._put({"name": name})
        self.name = name


class Hue:

    username = None
    bridge_ip = None

    def __init__(self, username=None, bridge_ip=None):
        if username is None:
            self._get_user()

        self.username = username
        self.bridge_ip = bridge_ip

    def get(self, uri=""):
        response = requests.get(f'https://{self.bridge_ip}/api{uri}', verify=False)
        return response

    def post(self, uri="", body=None):
        return requests.post(f'http://{self.bridge_ip}/api{uri}', body, verify=False)

    def put(self, uri="", body=None):
        print(f'http://{self.bridge_ip}/api{uri}')
        return requests.put(f'http://{self.bridge_ip}/api{uri}', data=body, verify=False)

    def _get_user(self):
        """
        Create a new user on the bridge
        :return: the username
        :rtype: str
        """
        response = self.post(uri="", body={"devicetype": "PhiliphsHue#AG"})
        print(response)
        if response is not None:
            print(response.json())
        # TODO self.username =

    def get_lights(self):
        """
        get all lights connected
        :rtype: list of Light
        """
        response = self.get(f'/{self.username}/lights')
        lights = []
        result = response.json()

        for key in result:
            lights.append(Light(sdk=self, light_id=key, **result[key]))

        return lights

    def get_groups(self):
        """
        get all lights groups
        """
        response = self.get(f'/{self.username}/groups')
        result = response.json()
        print(result)

        groups = []
        for key in result:
            groups.append(Group(sdk=self, group_id=key, **result[key]))

        return groups

    def on(self):
        """
        Turn on all the lights
        """
        pass

    def off(self):
        """
        Turn off all the lights
        """
        pass

