# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
WORDLIST = {
    "aaa": "AAA",
    "af": "AF",
    "api": "API",
    "arp": "ARP",
    "avd": "AVD",
    "bfd": "BFD",
    "bgp": "BGP",
    "cli": "CLI",
    "cos": "COS",
    "cpu": "CPU",
    "cvp": "CVP",
    "cvx": "CVX",
    "dc": "DC",
    "dhcp": "DHCP",
    "dns": "DNS",
    "dot1br": "dot1br",
    "dot1x": "dot1x",
    "dr": "DR",
    "dscp": "DSCP",
    "ecmp": "ECMP",
    "eos": "EOS",
    "evpn": "EVPN",
    "fcs": "FCS",
    "gnmi": "gNMI",
    "http": "HTTP",
    "icmp": "ICMP",
    "id": "ID",
    "ids": "IDs",
    "igmp": "IGMP",
    "igp": "IGP",
    "ip": "IP",
    "ipv4": "IPv4",
    "ipv6": "IPv6",
    "is": "IS",
    "isis": "ISIS",
    "lacp": "LACP",
    "lag": "LAG",
    "ldp": "LDP",
    "lfa": "LFA",
    "lldp": "LLDP",
    "lsa": "LSA",
    "l2": "L2",
    "mac": "MAC",
    "mcs": "MCS",
    "mgmt": "Management",
    "mib": "MIB",
    "mka": "MKA",
    "mlag": "MLAG",
    "mpls": "MPLS",
    "mtu": "MTU",
    "nd": "ND",
    "ntp": "NTP",
    "ospf": "OSPF",
    "pae": "PAE",
    "pbr": "PBR",
    "pes": "PEs",
    "pim": "PIM",
    "poe": "PoE",
    "ptp": "PTP",
    "pvlan": "PVLAN",
    "qos": "QOS",
    "ra": "RA",
    "rcf": "RCF",
    "regexp": "RegExp",
    "rp": "RP",
    "rps": "RPs",
    "rs": "RS",
    "rx": "RX",
    "sbfd": "SBFD",
    "sci": "SCI",
    "sha512": "SHA512",
    "spf": "SPF",
    "srlg": "SRLG",
    "ssh": "SSH",
    "ssl": "SSL",
    "svi": "SVI",
    "tcam": "TCAM",
    "tcp": "TCP",
    "terminattr": "TerminAttr",
    "ti": "TI",
    "tls": "TLS",
    "tlvs": "TLVs",
    "ttl": "TTL",
    "tx": "TX",
    "udp": "UDP",
    "url": "URL",
    "vlan": "VLAN",
    "vlans": "VLANs",
    "vmtracer": "VMTracer",
    "vn": "VN",
    "vpn": "VPN",
    "vrf": "VRF",
    "vrfs": "VRFs",
    "vrrp": "VRRP",
    "vxlan": "VxLAN",
    "ztp": "ZTP",
}


def key_to_display_name(key: str) -> str:
    if not isinstance(key, str):
        raise ValueError(f"Invalid argument passed to 'key_to_display_name'. Must be a string. Got '{type(key)}'")

    words = key.split("_")
    output = []
    for word in words:
        output.append(WORDLIST.get(word.lower(), word.title()))

    return " ".join(output)
