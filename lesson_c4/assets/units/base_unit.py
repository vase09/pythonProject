from __future__ import annotations
from abc import ABC

from lesson_c4.assets.equipment import Armor, Weapon
from lesson_c4.assets.classes import UnitClass


class BaseUnit(ABC):
    """Base class for units"""

    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        self.name = name
        self.unit_class = unit_class
        self.health_points_: float = unit_class.max_health
        self.stamina_points_: float = unit_class.max_stamina
        self.weapon = weapon
        self.armor = armor
        self.skill_used: bool = False
        
    @property
    def health_points(self):
        if self.health_points_ < 0:
            return 0
        return round(self.health_points_, 1)

    @property
    def stamina_points(self):
        return round(self.stamina_points_, 1)

    def attack(self, target: BaseUnit) -> str:
        """Attack logic"""
        if self.stamina_points_ >= self.weapon.stamina_per_hit:

            # Calculate and inflict damage on target
            damage_inflicted = self._calculate_damage(target)
            target._get_damage(damage_inflicted)

            # Update stamina points
            self.stamina_points_ -= self.weapon.stamina_per_hit
            target.stamina_points_ -= target.armor.stamina_per_turn

            # Ensure target stamina points greater than 0
            if target.stamina_points_ < 0:
                target.stamina_points_ = 0

            if damage_inflicted > 0:
                return (f"{self.name}, используя {self.weapon.name}, "
                        f"пробивает {target.armor.name} соперника и наносит {damage_inflicted} урона.")
            return (f"{self.name}, используя {self.weapon.name}, "
                    f"наносит удар, но {target.armor.name} соперника его останавливает.")

        return (f"{self.name} попытался использовать {self.weapon.name}, "
                f"но у него не хватило выносливости.")

    def use_skill(self, target: BaseUnit):
        """Use special skill"""
        if self.skill_used:
            return (f"{self.name} попытался использовать {self.unit_class.skill.name}, "
                    f"но навык уже был использован.")
        self.skill_used = True
        return self.unit_class.skill.use(user=self, target=target)

    def _calculate_damage(self, target: BaseUnit) -> float:
        """Calculate damage inflicted on target"""
        damage = self.weapon.calculate_damage() * self.unit_class.attack_modifier
        defence = target.armor.defence if target.stamina_points_ >= target.armor.stamina_per_turn else 0

        if damage <= defence:
            damage_inflicted = 0
        else:
            damage_inflicted = damage - defence

        return round(damage_inflicted, 1)

    def _get_damage(self, damage_inflicted: float) -> None:
        """Reduce health points for the amount of damage"""
        self.health_points_ -= damage_inflicted
