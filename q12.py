import json


class ConfigError(Exception):
    """Custom exception for configuration-related errors."""
    pass


def parse_config(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            config = json.load(file)

    except FileNotFoundError as e:
        raise ConfigError(f"Configuration file '{path}' was not found.") from e

    except json.JSONDecodeError as e:
        raise ConfigError(f"Configuration file '{path}' contains invalid JSON.") from e

    else:
        # Executed only if no exception occurred
        return config

    finally:
        # Executed regardless of success or failure
        print(f"Finished processing '{path}'.")


if __name__ == "__main__":
    try:
        config = parse_config("config.json")
        print("Configuration loaded successfully:")
        print(config)

    except ConfigError as e:
        print(f"Error: {e}")