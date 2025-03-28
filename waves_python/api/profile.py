from enum import Enum


class Profile(Enum):
    MAINNET = "https://nodes.mdmcoin.com"
    STAGENET = "https://nodes-stagenet.mdmcoin.com"
    TESTNET = "https://nodes-testnet.mdmcoin.com"
    LOCAL = "http://127.0.0.1:7879"
