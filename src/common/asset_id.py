from typing import List

from pydantic import Field

from src.model.node_model import NodeModel
from src.util import base58_utils

BYTE_LENGTH = 32
WAVES_STRING = "WAVES"


class AssetId:
    base58_string = Field()

    @classmethod
    def from_str(cls, encoded: str):
        address = cls()
        address.base58_string = base58_utils.from_string(encoded)
        return address

    def to_str(self):
        return base58_utils.to_string(self.base58_string)

    class Config:
        arbitrary_types_allowed = True


class AssetIds(NodeModel):
    asset_ids: List[AssetId]

    class Config:
        arbitrary_types_allowed = True
