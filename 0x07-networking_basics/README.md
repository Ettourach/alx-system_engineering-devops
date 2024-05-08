#!/usr/bin/env bash

# readme file for folder 0x07-networking_basics

# input for project
i must know all concepts about:
OSI Model
What it is
How many layers it has
How it is organized
What is a LAN
Typical usage
Typical geographical size
What is a WAN
Typical usage
Typical geographical size
What is the Internet
What is an IP address
What are the 2 types of IP address
What is localhost
What is a subnet
Why IPv6 was created
TCP/UDP
What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
What is the main difference between TCP and UDP
What is a port
Memorize SSH, HTTP and HTTPS port numbers
What tool/protocol is often used to check if a device is connected to a network

# requirements 

0. OSI model
on this tasks i will giving the answer for two questions 
1-what is OSI model
2-How is the OSI model organized?

1. Types of network
i have three questions
1-What type of network a computer in local is connected to?
2-What type of network could connect an office in one building to another office in a building a few streets away?
3-What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

2. MAC and IP address
two questions
1-What is a MAC address?
2-What is an IP address?

3. UDP and TCP
three questions
1-Which statement is correct for the TCP box:
It is a protocol that is transferring data in a slow way but surely
It is a protocol that is transferring data in a fast way and might loss data along in the process
2-Which statement is correct for the UDP box:
It is a protocol that is transferring data in a slow way but surely
It is a protocol that is transferring data in a fast way and might loss data along in the process
3-Which statement is correct for the TCP worker:
Have you received boxes x, y, z?
May I increase the rate at which I am sending you boxes?

4. TCP and UDP ports
in this task i will reating a Bash script that displays listening ports:
That only shows listening sockets
That shows the PID and name of the program to which each socket belongs

5. Is the host on the network
i must reating  a Bash script that pings an IP address passed as an argument.
Accepts a string as an argument
Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
Ping the IP 5 times
