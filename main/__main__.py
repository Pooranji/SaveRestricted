import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import bot

# Define the host and port
HOST = '0.0.0.0'  # Use 'localhost' or '127.0.0.1' for local testing
PORT = 8080       # Example port number

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    try:
        patt = Path(name)
        plugin_name = patt.stem
        load_plugins(plugin_name)
        logging.info(f"Loaded plugin: {plugin_name}")
    except Exception as e:
        logging.error(f"Failed to load plugin {name}: {e}")

print("Successfully deployed!")
print("By MaheshChauhan • DroneBots")

if __name__ == "__main__":
    # Assuming your bot's run method accepts host and port
    bot.run_until_disconnected(host=HOST, port=PORT)
