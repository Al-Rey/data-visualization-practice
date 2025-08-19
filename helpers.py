import json
from pathlib import Path

CONFIG_PATH = DATA_DIR = Path().resolve() / "config.json"


def get_mysql_config():
    with open(CONFIG_PATH, "r") as ff:
        config = json.load(ff)["mysql"]


    url = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:3306/{config['database']}"
    return url



if __name__ == '__main__':
    print(get_mysql_config())