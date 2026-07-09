import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    return json.loads(REPORT.read_text())


def test_report_is_valid_json_object():
    # criterion 1: report exists and is a single JSON object
    assert REPORT.exists(), "no /app/report.json found"
    assert isinstance(load_report(), dict), "report.json is not a JSON object"


def test_report_has_exact_keys():
    # criterion 2: only the three required keys
    data = load_report()
    assert set(data) == {"total_requests", "unique_ips", "top_path"}, sorted(data)


def test_total_requests():
    # criterion 3: total_requests == number of non-blank log lines
    data = load_report()
    assert isinstance(data["total_requests"], int)
    assert data["total_requests"] == 6, data["total_requests"]


def test_unique_ips():
    # criterion 4: unique_ips == number of distinct client IPs
    data = load_report()
    assert isinstance(data["unique_ips"], int)
    assert data["unique_ips"] == 3, data["unique_ips"]


def test_top_path():
    # criterion 5: top_path == most frequently requested path
    data = load_report()
    assert isinstance(data["top_path"], str)
    assert data["top_path"] == "/index.html", data["top_path"]
