from typing import List
from dataclasses import dataclass


from .utils import MythicBase

@dataclass
class MythicSkill(MythicBase):
    unique_id: str
    cooldown: int
    skills: List[str]
