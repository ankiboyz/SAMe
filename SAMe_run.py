# SAMe_run.py
"""
This is file which is the starting point for the SAMe APP.
This will trigger the application run.
"""
import config
from flask import Flask
import logging
import SAMe_app

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    print(__name__)

app_SAMe = SAMe_app.create_app()

try:
    # with host="0.0.0.0" argument the up application is run on all IPs of this server
    # and can be reached from the external world.
    # appln.run(host="0.0.0.0", port='50008')
    app_SAMe.run(host=config.HOST_IP, port=config.PORT)
    print("I am Here: running")

finally:
    logger.info("Finally block in the application stop ")
    print("Finally block in the application stop ")  # in case logger is not initialized when the application stops