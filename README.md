# Simple: IP Addressing

## Description

This is a simple Python script I created during my CISCO Networking course to verify that my IP addressing calculations are correct. It allows you to input an IP address and the number of hosts for each network, then calculates the necessary subnet information.

## How to Use

1. Open your terminal.
2. Navigate to the directory where `IP_Addressing.py` is located.
3. Run the script by typing:


4. Follow the prompts to enter the IP address and the number of hosts for each network.

## Example

When you run the script, it will ask for an IP address and the number of hosts for each network, separated by commas. Here's a sample interaction:

```bash
python IP_Addressing.py
```

![Recording 2024-08-09 105544](https://github.com/user-attachments/assets/b7ec7782-16b7-45f0-ae0f-643944bcf6d8)

**Input:**

```plaintext
IP Address: 192.168.100.10
Enter the Hosts separated with commas: 500,100,50
```

**Output:**

```plaintext
============================================================
Result for 192.168.100.10 with 500 hosts
Number of hosts = 500
(2^n)-2 >= 500
N       = 9
2^n     = 512
11111111.11111111.11111110.00000000
Subnet Mask Length      = 32 - 9 = 23
Subnet Mask Value       = 255.255.254.0
Network Address = 192.168.100.10 / 23
First Valid Host Address        = 192.168.100.11
Last Valid Host Address = 192.168.102.8
Broadcast Address       = 192.168.102.9
============================================================

Result for 192.168.102.10 with 100 hosts
Number of hosts = 100
(2^n)-2 >= 100
N       = 7
2^n     = 128
11111111.11111111.11111111.10000000
Subnet Mask Length      = 32 - 7 = 25
Subnet Mask Value       = 255.255.255.128
Network Address = 192.168.102.10 / 25
First Valid Host Address        = 192.168.102.11
Last Valid Host Address = 192.168.102.136
Broadcast Address       = 192.168.102.137
============================================================

Result for 192.168.102.138 with 50 hosts
Number of hosts = 50
(2^n)-2 >= 50
N       = 6
2^n     = 64
11111111.11111111.11111111.11000000
Subnet Mask Length      = 32 - 6 = 26
Subnet Mask Value       = 255.255.255.192
Network Address = 192.168.102.138 / 26
First Valid Host Address        = 192.168.102.139
Last Valid Host Address = 192.168.102.200
Broadcast Address       = 192.168.102.201
============================================================
```

## Notes

- The script calculates the number of required bits for the subnet mask based on the number of hosts.
- It then outputs the subnet mask, network address, first and last valid host addresses, and the broadcast address for each subnet.

Feel free to modify and extend this script as needed for your networking studies or projects!
```
