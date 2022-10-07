from dataclasses import dataclass

import marshmallow
import marshmallow_dataclass


@dataclass
class Armor:
    """Class for armor"""
    name: str
    defence: float
    stamina_per_turn: float

    class Meta:
        unknown = marshmallow.EXCLUDE


ArmorSchema = marshmallow_dataclass.class_schema(Armor)
