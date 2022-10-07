from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lesson_c4.assets.units import BaseUnit


class BaseSkill(ABC):
    """Base class for special skills"""
    name: str = ""
    damage: float = 0
    stamina_required: float = 0
    user: BaseUnit
    target: BaseUnit

    @abstractmethod
    def _skill_effect(self):
        pass

    def use(self, user: BaseUnit, target: BaseUnit):
        """Use special skill if user has enough stamina"""
        self.user = user
        self.target = target

        if self.user.stamina_points_ < self.stamina_required:
            return (f"{self.user.name} попытался использовать {self.user.unit_class.skill.name}, "
                    f"но у него не хватило выносливости.")
        return self._skill_effect()
