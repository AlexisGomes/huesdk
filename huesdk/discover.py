import json
import requests
import socket
import time
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

mdns_bridges = []

class mDNSListener(ServiceListener):
    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        global mdns_bridges
        info = zc.get_service_info(type_, name)
        mdns_bridges.append(info)

class Discover:

    def __init__(self,discovery_url="https://discovery.meethue.com"):
        self.discovery_url = discovery_url

    def find_hue_bridge(self):
        response = requests.get(self.discovery_url, verify=False)

        result = response.json()
        if result and type(result) is list and "error" in result[0] and result[0]["error"]:
            raise Exception(result[0]["error"]["description"])        

        return json.dumps(result, indent=4)

    def find_hue_bridge_mdns(self, timeout=5):
        zeroconf = Zeroconf()
        listener = mDNSListener()
        # search for bridges
        browser = ServiceBrowser(zeroconf, "_hue._tcp.local.", listener)
        # wait for timeout
        time.sleep(timeout)
        zeroconf.close()
        bridges = []
        for bridge in mdns_bridges:
            bridge_id = bridge.server.split(".")[0]
            
            # Attempt to resolve IP with different formats
            formats_to_try = [
                bridge.server,                   # Original server name
                bridge.server.rstrip('.'),       # Remove trailing dot if exists
                f"{bridge_id}.local"             # Append '.local' to the bridge ID
            ]

            for fmt in formats_to_try:
                try:
                    bridge_ip = socket.gethostbyname(fmt)
                    break
                except socket.gaierror:
                    continue  # Try the next format if an error occurs
                
            bridge_name = bridge.name.split(".")[0]
            bridge_info = {
                "internalipaddress": bridge_ip,
                "id": bridge_id,
                "name": bridge_name
            }
            bridges.append(bridge_info)
        return json.dumps(bridges, indent=4)
