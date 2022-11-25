# ShrimpyRewrite
A rewrite of Shrimpy to make use of the new and updated Discord functionality and Pycord v2.3's implementation of it.

## Self-Hosting Shrimpy
In order to self host Shrimpy, there are a few requirements that need to be satisfied:
- A Discord account with an application configured in the [Developer Portal](https://discord.com/developers/docs/getting-started)
- [Python](https://www.python.org/downloads/release/python-3110/) must be installed (I suggest Python 3.11 as it is the version I am presently targetting)
- [Pycord 2.3.0](https://github.com/Pycord-Development/pycord)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
Once you have all of these things complete, you must create a file titled ".env" in the root directory of Shrimpy. This file should look like the following:
```.env
env title=".env"
TOKEN="insert your personal application secret token here between the quotes"
OWNER=insert your personal discord id here
```
After creating this file and inserting the corresponding data, you are good to start running Shrimpy by running the following command in the command line:
```python3 main.py```.
Or, you can double click on main.py (on supported systems) and Shrimpy will startup. (Please note that by starting the bot with this method, you may find that if a crash occurs, Shrimpy's output will not remain open).
