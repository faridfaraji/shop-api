
from dataclasses import dataclass, asdict

from typing import List


@dataclass
class Doc:
    document: str
    doc_type: str = None
    doc_identifier: str = None
    hash: str = None
    embedding: List[float] = []
    storage_status: str = None
    id: str = None

    meta_keys = ["storage_status"]

    def to_dict(self):
        return {k: v for k, v in asdict(self).items() if k != self.meta_keys}
