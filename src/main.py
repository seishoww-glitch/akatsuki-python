import json
import datetime


def create_measurement():
    measurement = {
        "timestamp": datetime.datetime.now().isoformat(),
        "tps": 20.0,
        "mspt": 45.2,
        "player_count": 5,
        "cpu_percent": 75.5,
        "ram_percent": 34.3,
    }

    return measurement

def create_dump():
    json.dump()
def main():
    measurement = create_measurement()
    print(measurement)


if __name__ == "__main__":
    main()

def tps_check():

    return 

def errors():
    measurement = create_measurement()    