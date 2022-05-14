from hummingbot.client.config.config_var import ConfigVar
from hummingbot.client.settings import required_exchanges

CENTRALIZED = False
EXAMPLE_PAIR = "LUNA-UST"
DEFAULT_FEES = [0., 0.]


KEYS = {
    "automask_wallet_address":
        ConfigVar(key="automask_wallet_address",
                  prompt="Enter your wallet address >>> ",
                  required_if=lambda: "automask" in required_exchanges,
                  is_secure=True,
                  is_connect_key=True),
    "automask_wallet_seeds":
        ConfigVar(key="automask_wallet_seeds",
                  prompt="Enter your wallet seeds >>> ",
                  required_if=lambda: "automask" in required_exchanges,
                  is_secure=True,
                  is_connect_key=True),
}
