#!/bin/bash

# File containing the list of IP addresses to ping
ip_file="ip_addresses.txt"

# List of network interfaces to use
interfaces=("10.1.1.11" "10.1.2.11" "10.1.3.11" "10.1.4.11")

# Check if the IP file exists
if [ ! -e "$ip_file" ]; then
  echo "Error: IP address file '$ip_file' not found!"
  exit 1
fi

# Read the IP addresses from the file into an array
ip_addresses=()
while IFS= read -r ip; do
  ip_addresses+=("$ip")
done < "$ip_file"

# Loop through each IP address
for ip in "${ip_addresses[@]}"; do
  # Loop through each network interface
  for iface in "${interfaces[@]}"; do
    # Ping the IP address from the network interface
#    ping -c 2 -I "$iface" "$ip"
     code=`ping -c 2 -W 3 -I "$iface" "$ip"|grep loss|awk '{print $6}'|awk -F "%" '{print $1}'`
     if [ $code -eq 0 ]; then
        echo -e "\033[32m ping  $ip from $iface \t Success  \t\t packet loss: %$code \033[0m"
     else
        echo -e "\033[31m ping  $ip from $iface \t Fail     \t\t packet loss: %$code \033[0m"
#    echo "Ping result from $iface to $ip: $?"
     fi
  done
done
