from typing import List
from dataclasses import dataclass


from .utils import MythicBase

@dataclass
class MythicMob(MythicBase):
    unique_id: str
    mob_type: str
    display: str
    health: int
    damage: int
    armor: int
    bossbar: dict
    faction: str
    mount: str
    options: dict
    modules: dict
    goal_selectors: List[str]
    target_selectors: List[str]
    drops: List[str]
    damage_modifiers: List[str]
    equipment: dict
    kill_messages: List[str]
    level_modifiers: List[str]
    skills: List[str]
