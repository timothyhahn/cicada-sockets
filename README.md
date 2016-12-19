# Cicada Sockets
[![Build Status](https://travis-ci.org/timothyhahn/cicada-sockets.svg?branch=master)](https://travis-ci.org/timothyhahn/cicada-sockets)
[![Coverage Status](https://coveralls.io/repos/github/timothyhahn/cicada-sockets/badge.svg)](https://coveralls.io/github/timothyhahn/cicada-sockets)

Simple websocket broadcast-er. Hoping to turn this into a little fun side project.

## Installation

```
$ virtualenv venv -p <insert_path_here>/python3.4 # Or just use virtualenvwrapper, tbh.
$ source venv/bin/activate # OR JUST USE VIRTUALENVWRAPPER, TBH
$ pip install -r requirements.txt
$ tox # To make sure things are correctly setup
$ python app.py # To run the server
$ # Point the webapp to this service (default is currently :8888)
```
