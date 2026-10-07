from src.coldchain import Cabinet, LOG_EVERY_SEC


def test_log_intervalo_y_puerta():
    c = Cabinet("f1", temp_c=-12.0, door_open=False)
    assert c.should_log(0) is True
    assert c.should_log(LOG_EVERY_SEC - 1) is False
    assert c.should_log(LOG_EVERY_SEC) is True
    c.door_open = True
    ok, motivo = c.vend_allowed()
    assert ok is False
    assert motivo == "door open"


def test_linea_de_log():
    c = Cabinet("f1", temp_c=-12.0, door_open=False)
    linea = c.log_line(300)
    assert "f1" in linea
    assert "-12.0C" in linea
    assert "puerta=cerrada" in linea
    assert "venta=True" in linea
