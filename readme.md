# A hacky solution to watching website changes

I'm using this project to get notified when practice room passes are available, as published on [this website](https://www.eca.ed.ac.uk/facility/music-practice-rooms-and-instruments).

## How does it work?

The main script `web_watcher.py` pulls targeted content from the website lying at the desired URL.
It compares it with a local cache file, and notifies the user if there are any changes.

On Linux-based systems, you can schedule periodic script execution using crontab.

## Caveats

There are plenty of solutions out there which have:
* A better notification system
* A better content targeting system

This project is more of a proof of concept to myself.
