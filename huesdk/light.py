import json

from huesdk.generics import hexa_to_xy


class Light:

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

    def on(self, transition=4):
        if self.is_on is False:

            # by default when the APP starts and the lights were off, the brightness will be set to 1
            if self.bri == 1:
                self.bri = 254

            self._put_state({
                "on": True,
                "bri": self.bri,  # by default the API, set the value to 1
                "transitiontime": transition,
            })
            self.is_on = True

    def off(self, transition=4):
        if self.is_on is True:
            self._put_state({"on": False, "transitiontime": transition})
            self.is_on = False

    def set_brightness(self, value, transition=4):
        if value < 1 or value > 254:
            raise Exception("Invalid brightness value. It should be between 1 and 254")
        self._put_state({"bri": value, "transitiontime": transition})
        self.bri = value

    def set_saturation(self, value, transition=4):
        self._put_state({"sat": value, "transitiontime": transition})

    def set_color(self, hue=None, hexa=None, transition=4):
        if hue is not None:
            self._put_state({"hue": hue, "transitiontime": transition})
        elif hexa is not None:
            xy = hexa_to_xy(hexa)
            self._put_state({"xy": xy, "transitiontime": transition})

    def set_name(self, name):
        self._put({"name": name})
        self.name = name