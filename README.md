# probereq
Simple probe request script made using python and scapy.

![Picture](images/probereq.png)

# Usage
Firstly you need to ```sudo airmon-ng start [Interface name] ``` and follow the prompts to get your device into monitor mode.

After your device is in monitor mode you can use ```sudo python2 probereq.py -i [Interface name] ```.
Then it will ask if you want "Broadcast probes." Broadcast probes do not contain an SSID only a MAC from the device it's coming from.

The script also creates a file called ```probes.txt ``` in the directory you run the script in. It prints whatever the terminal does to a file. For when you want to go back and look at what you scanned.
I find this easier than saving an entire pcap file.

To quit, just ```Ctrl+C```

# Dependencies
These can be installed with pip ```pip install [package]```

1. manuf
2. argparse
3. scapy

# Contributing

If you would like to contribute or suggest any improvements to the project, please submit a merge request.


# License

[GNU General Public License, version 3 (GPLv3)](https://www.gnu.org/licenses/gpl.txt)

