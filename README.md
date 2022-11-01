# huesdk

Python package to control the Philips Hue lights.

Make the usage of the Philips Hue API 1.0 easier with an object-oriented structure.

## Installation

```
pip install huesdk
```

## Discovery

To find the IP of your hue bridge, go to https://discovery.meethue.com. Or alternatively,

```python
from huesdk import Discover
discover = Discover()
print(discover.find_hue_bridge())
```

Since https://discovery.meethue.com and ```discover.find_hue_bridge()``` are rate limited
and require an internet connection, you can also search for bridges locally using mDNS:

```python
from huesdk import Discover
discover = Discover()
print(discover.find_hue_bridge_mdns(timeout=5))
```


## Connexion

```python
from huesdk import Hue
# For the first usage 
# Press your bridge button
# the connect method will return a username
username = Hue.connect(bridge_ip=YOUR_BRIDGE_IP)

# You can now create an instance of the Hus class, 
# next you won't need to press the button
hue = Hue(bridge_ip=YOUR_BRIDGE_IP, username=YOUR_USERNAME)

# Turn on all the lights
hue.on()

# Turn off all the lights
hue.off()
```

## Lights

### Get all light objects
```python
lights = hue.get_lights()

# Print light properties
for light in lights:
    print(light.id_)
    print(light.name)
    print(light.is_on)
    print(light.bri)
    print(light.hue)
    print(light.sat)

# turn on each lights
for light in lights:
    light.on()
```

### Get single light
```python
# get light with id
light = hue.get_light(id_=1)

# get light with name
light = hue.get_light(name="Room 1")
```

### Lights methods
```python
lights = hue.get_lights()

# turn on
lights[0].on()

# turn off
lights[0].off()

# Change color 
# with hue, red=65535, green=21845 and blue=43690
lights[0].set_color(hue=43690)

# with hexadecimal
lights[0].set_color(hexa="#065535")

# Change brightness, from 1 to 254
lights[0].set_brightness(254)

# Change light's name
lights[0].set_name("Hue color lamp 2")

# Change saturation, from 1 to 254
lights[0].set_saturation(254)
```
### Transitions
For each change, you can set a transition time.
This is given as a multiple of 100ms. 
So `transition=10` will make the transition last 1 second.
The default value is 4 (400ms).

```python
light = hue.get_light(name="kitchen")

# the light will slowly turn off in 5secs
light.off(transition=50)

# the light will be red after 10 seconds
light.set_color(hexa="#ff0000", transition=100)
```

## Groups
The same methods are available for groups

### Get all group objects
```python
groups = hue.get_groups()

# Print light properties
for group in groups:
    print(group.id_)
    print(group.name)

# turn on each groups
for group in groups:
    groups.on()
```

### Get single group
```python
# get group with id
group = hue.get_group(id_=1)

# get group with name
group = hue.get_group(name="kitchen")
```

### Groups methods
```python
groups = hue.get_groups()

# turn on
groups[0].on()

# turn off
groups[0].off()

# Change brightness, from 1 to 254
groups[0].set_brightness(value)

# Change group's name
groups[0].set_name("Hue color lamp 2")

# Change saturation, from 1 to 254
groups[0].set_saturation(value)
```

### Transitions
Transitions are also available for groups.
```python
group = hue.get_group(name="kitchen")
group.off(transition=1000)
```

## Schedules

### Get all schedules objects
```python
schedules = hue.get_schedules()

# Print schedules properties
for schedule in schedules:
    print(schedule.id_)
    print(schedule.name)
    print(schedule.description)
    print(schedule.status)
    print(schedule.command)
```

### Schedules methods
```python
schedules = hue.get_schedules()

# Change name
schedules[0].set_name("Schedules 0")
# Change description
schedules[0].set_description("Schedules 0")

# Delete
schedules[0].delete()
```