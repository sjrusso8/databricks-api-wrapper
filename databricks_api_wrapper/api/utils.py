import configparser
from pathlib import Path


# this will need to be switched to ENV vars or a .env file
def databricks_confg():
    cfg_file = [v for v in Path.home().glob(
        "*.databrickscfg") if v.is_file()][0]

    config = configparser.ConfigParser()

    config.read(cfg_file)

    return {
        "host": config.get("DEFAULT", "host"),
        "token": config.get("DEFAULT", "token")
    }
