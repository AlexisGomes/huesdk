import json

from huesdk.generics import hexa_to_xy


class Group:

    sdk = None

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

    def on(self, transition=4):
        if self.is_on is False:
            self._put_action({"on": True, "transitiontime": transition})
            self.is_on = True

    def off(self, transition=4):
        if self.is_on is True:
            self._put_action({"on": False, "transitiontime": transition})
            self.is_on = False

    def set_brightness(self, value, transition=4):
        self._put_action({"bri": value, "transitiontime": transition})

    def set_saturation(self, value, transition=4):
        self._put_action({"sat": value, "transitiontime": transition})

    def set_color(self, hue=None, hexa=None, transition=4):
        if hue is not None:
            self._put_action({"hue": hue, "transitiontime": transition})
        elif hexa is not None:
            xy = hexa_to_xy(hexa)
            self._put_action({"xy": xy, "transitiontime": transition})

    def set_name(self, name):
        self._put({"name": name})
        self.name = name