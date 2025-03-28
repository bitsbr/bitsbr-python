from enum import Enum


class Profile(Enum):
    MAINNET = "https://nodes.bitsbr.org"
    STAGENET = "https://nodes-stagenet.bitsbr.org"
    TESTNET = "https://nodes-testnet.bitsbr.org"
    LOCAL = "http://127.0.0.1:9899"
