from dataclasses import dataclass, field


@dataclass
class EquipmentData:
    """Storage for weapons and armor"""
    weapons: list = field(default_factory=list)
    armor: list = field(default_factory=list)
