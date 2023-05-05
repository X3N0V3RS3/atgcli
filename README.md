# atgcli
A command line interface tool for Veeder Root Automated Tank Guages that sends commands to each IP Address
in a list and comes with Three modes

Usage:
Default: Runs a basic GetInventory Request and sends data back
Info: Runs any info gathering command for example: I20100, I40100 I60100 (check the manual)
Set: Runs any reconfiguration command for example: s60200Gas Station(Changes name) s601000(Turns off all Tank configurations)

Put all Target IP Addresses in atglist.txt

Link to the Manual:https://cdn.chipkin.com/files/liz/576013-635.pdf
I = Info and s = Set 

This tool can also be run alongside Proxychains for Pentesting and Anonimity Purposes
