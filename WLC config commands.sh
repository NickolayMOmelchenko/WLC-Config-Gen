WLC config commands

enable
configure terminal

aaa new-model - Enable AAA Configuration on WLC.
1) radius server <name>	- name of the RADIUS server configuration 
2) address ipv4 <radius-server-ip> auth-port 1812 acct-port 1813 - set communication to the AAA server
timeout 300
retransmit 3
3) key <shared-key> - set a shared key for secure commination (must match shared key on ISE)
exit

4)aaa group server radius <radius-grp-name> - Add AAA server to the group
5)server name <radius-server-name> - why
exit
aaa server radius dynamic-author
6-)client <radius-server-ip> server-key <shared-key>
6)aaa authentication dot1x <dot1x-list-name> group <radius-grp-name>
radius-server dead-criteria time 5 tries 3
radius-server deadtime 5

// ********
WLAN Profile Conifig 
config t
wlan <profile-name> <wlan-id> <ssid-name> 
security dot1x authentication-list <dot1x-list-name>
no shutdown

config t
wireless profile policy <policy-profile-name>
aaa-override
central switching
vlan <vlanID-or-VLAN_name>
no shutdown

config t
wireless tag policy <policy-tag-name>
wlan <profile-name> policy <policy-profile-name>

config t
ap <ethernet-mac-addr>
policy-tag <policy-tag-name>
end

ISE config from here on out 