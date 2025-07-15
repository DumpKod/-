import json
from alephnet.json_interface import validate_response_format

def test_template_response():
    with open("agent_io/template_response.json") as f:
        data = json.load(f)
    assert validate_response_format(data), "Invalid JSON structure"
