import json

def validate_response_format(response):
    required_fields = {"task_id", "model", "responses"}
    if not all(field in response for field in required_fields):
        return False
    return True
