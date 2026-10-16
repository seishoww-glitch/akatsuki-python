
import json
import datetime
from pathlib import Path

# Store the data beside this Python script
DATA_FILE = Path(__file__).with_name("measurements.json")


def load_measurements():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Expected a list of measurements.")

        return data

    except (json.JSONDecodeError, ValueError) as error:
        print(f"Error reading saved data: {error}")
        raise


def save_measurements(measurements):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(measurements, file, indent=4)


def collect_measurement():
    """Create one sample measurement."""
    return {
        "timestamp": datetime.datetime.now().astimezone().isoformat(),
        "tps": 20.0,
        "mspt": 45.2,
        "player_count": 5,
        "cpu_percent": 75.5,
        "ram_percent": 34.3,
    }


def main():
    measurements = load_measurements()

    new_measurement = collect_measurement()
    measurements.append(new_measurement)

    save_measurements(measurements)

    print("Measurement saved successfully.")
    print(f"Total measurements: {len(measurements)}")
    print(f"Saved to: {DATA_FILE}")
    print("\nLatest measurement:")
    print(json.dumps(new_measurement, indent=4))


if __name__ == "__main__":
    main()
