# Hardware — Android como base

Repo: open-vending-frozen. Distinto de open-vending. No fusionar.

## Que controla este repo

Cadena de frio (`src/coldchain.py`): no vender si esta caliente o la puerta abierta.
Android es HMI. El corte lo decide el sensor + Python.

## Hardware minimo

- Panel Android industrial, 12–24 V, kiosco.
- NTC o DS18B20 en la camara fria.
- Sensor de puerta (reed / fin de carrera).
- Relé de compresor / lockout si sale de rango.
- NTP. Sin hora, el frio no se audita.

Intemperie: IP65 y rango termico real. Tablet de living no.

Licencia MIT. Lee `/LEEME_LICENCIA.md`. Sin garantia.
