"""Lock vend if cabinet temperature is out of range.
"""
from dataclasses import dataclass

@dataclass
class Cabinet:
    id: str
    temp_c: float
    min_c: float = -18.0
    max_c: float = 4.0
    door_open: bool = False

    def healthy(self) -> bool:
        if self.door_open:
            return False
        return self.min_c <= self.temp_c <= self.max_c

    def vend_allowed(self) -> tuple[bool, str]:
        if self.door_open:
            return False, "door open"
        if self.temp_c > self.max_c:
            return False, "too warm"
        if self.temp_c < self.min_c:
            return False, "too cold / sensor"
        return True, "ok"
