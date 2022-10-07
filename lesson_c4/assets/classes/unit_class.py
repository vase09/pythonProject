from abc import ABC
from dataclasses import dataclass

from lesson_c4.assets.skills import BaseSkill


@dataclass
class UnitClass(ABC):
    """Dataclass for unit classes"""
    name: str
    max_health: float
    max_stamina: float
    attack_modifier: float
    stamina_modifier: float
    armor_modifier: float
    skill: BaseSkill
