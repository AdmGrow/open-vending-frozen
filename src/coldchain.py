"""Si esta caliente o la puerta abierta, no vendo.
Los numeros -18 y 4 los copie de internet, no se si estan bien.
"""
from dataclasses import dataclass

LOG_EVERY_SEC = 300  # 5 minutos. No se si es el intervalo correcto.


@dataclass
class Cabinet:
    id: str
    temp_c: float
    min_c: float = -18.0
    max_c: float = 4.0
    door_open: bool = False
    last_log_sec: int = 0

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

    def should_log(self, now_sec: int) -> bool:
        if now_sec - self.last_log_sec < LOG_EVERY_SEC:
            return False
        self.last_log_sec = now_sec
        return True

    def log_line(self, now_sec: int) -> str:
        ok, motivo = self.vend_allowed()
        puerta = "abierta" if self.door_open else "cerrada"
        return f"{now_sec}s {self.id} {self.temp_c}C puerta={puerta} venta={ok} ({motivo})"
