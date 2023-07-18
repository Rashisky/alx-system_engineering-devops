#!/usr/bin/bash
Firewall (ufw -> Uncomplicated Firewall)
This is a command line tool used for managing firewall rules in Ubuntu and other linux distributions. Firewall itself is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.
Commands used in ufw include: (sudo)
ufw enable
ufw disable
ufw default [allow|deny]
ufw allow/deny port
ufw status
ufw status verbose
ufw allow from [IP] to any port [Port]
ufw delete [rule_number]
ufw reload
ufw app list
ufw numbered
ufw --help
