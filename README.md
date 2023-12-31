# atgcli
A command line interface tool for Veeder Root Automated Tank Gauges that sends commands to each IP Address in a list and comes with two modes.

## Commands

For information about the functions that the Veeder-Root automatic tank gauge systems take, please refer to https://cdn.chipkin.com/files/liz/576013-635.pdf.

## Usage

You will first want to download this repository and enter target IP addresses into ``atglist.txt``. Once you have done this, run ``atgcli.py``.

You will be prompted to select a mode. There are two modes you can use this CLI tool with:
- Default: Runs a basic Get Inventory Request and sends data back as bytecode.
- Execute: Runs a user-defined function and sends it back as bytecode.

Once you have selected a mode, the program should carry out that process for all the targets you provided. This tool can also be run alongside Proxychains for pentesting and anonimity purposes.
