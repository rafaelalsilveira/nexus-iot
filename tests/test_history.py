from nexus import main


def test_load_history_when_file_does_not_exist(tmp_path, monkeypatch):
    history_file = tmp_path / "devices_history.json"
    monkeypatch.setattr(main, "HISTORY_FILE", history_file)

    assert main.load_history() == {}


def test_save_and_load_history(tmp_path, monkeypatch):
    history_file = tmp_path / "devices_history.json"
    monkeypatch.setattr(main, "HISTORY_FILE", history_file)

    history = {
        "AA:BB:CC:DD:EE:FF": {
            "name": "Dispositivo de teste",
            "detections": 3
        }
    }

    main.save_history(history)

    assert main.load_history() == history


def test_load_history_with_invalid_json(tmp_path, monkeypatch):
    history_file = tmp_path / "devices_history.json"
    monkeypatch.setattr(main, "HISTORY_FILE", history_file)

    history_file.write_text("{ json inválido", encoding="utf-8")

    assert main.load_history() == {}
