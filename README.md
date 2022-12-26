# ShrimpyRewrite
A rewrite of Shrimpy to make use of the new and updated Discord functionality and Pycord v2.3's implementation of it.

## What is Shrimpy?
Shrimpy is a Discord bot that I began writing during the pandemic. I was in the process of finishing up my associate's degree in software development and was eager to begin developing a project that I could continue to improve my programming skills and have something to include on my portfolio.

What followed is Shrimpy, a not-so-impressive Discord bot written in py-cord. As time goes on, I hope to make Shrimpy a more complex and well-thought-out bot. 

## Self-Hosting Shrimpy
In order to self-host Shrimpy, there are a few requirements that need to be satisfied:
- A Discord account with an application configured in the [Developer Portal](https://discord.com/developers/docs/getting-started)
- [Python 3](https://www.python.org/downloads/release/python-3110/) must be installed (I suggest Python 3.11 as it is the version I am presently targetting)
- [Pycord 2.3.2](https://github.com/Pycord-Development/pycord)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
Once you have all of these things complete, you must create a file titled ".env" in the root directory of Shrimpy. This file should look like the following:
```.env
env title=".env"
TOKEN="insert your personal application secret token here between the quotes"
OWNER=insert your personal discord id here
```
After creating this file and inserting the corresponding data, you are good to start running Shrimpy by running the following command in the command line:
```python3 main.py```.
Or, you can double-click on main.py (on supported systems) and Shrimpy will start. (Please note that by starting the bot with this method, you may find that if a crash occurs, Shrimpy's output will not remain open).

## Shrimpy Versioning
Shrimpy makes use of [semantic versioning](https://semver.org). However, as Shrimpy is still in early development, the versioning method will be subject to change throughout. As of now Shrimpy's versioning will work as follows:

<p align="center">X.Y.Z</p>

X represents a major revision. As of now, these revisions will occur *after* Shrimpy leaves an alpha state and will represent significant changes to Shrimpy. 

Y represents minor releases, these will often contain small new features and bug fixes. 

Z will represent bug fix releases. These will generally contain no new features and will be dedicated to fixing issues (software and linguistic) relating to Shrimpy.