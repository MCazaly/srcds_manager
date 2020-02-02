# SRCDS Manager

A very simple utility for automatically restarting containerised SRCDS instances when they have no online players.

Tested with Python 3.7, requires [python-a2s](https://github.com/Yepoleb/python-a2s) by [Yepoleb](https://github.com/Yepoleb).
# Why?
SRCDS instances tend to become "choppy" or "jittery" after being left running for a while. The obvious solution is regularly and automatically restart the server, but that risks disrupting players, so I wrote this tool to only restart the server is no one is currently playing on it.
# Usage
Running install.sh creates a virtual environment and a servers.json file. Populate the JSON file with your server details in the format:
```json
{
  "container_name": {
    "host": "example.com",
    "port": 27015
  }
}
```
Then you can simply execute auto_restart.sh as desired, probably in a cron job.
