def log_contribution(agent, task_id, T_x):
    return {
        "version": "1.2.0",
        "type": "hypothesis",
        "cycle": 6,
        "agent": {"name": agent, "role_description": "External φⁿ agent"},
        "core": {
            "contribution": {
                "type": "answer",
                "description": f"Ответ на задачу {task_id}",
                "T_x": {
                    "value": T_x,
                    "method": "external_model_estimation"
                }
            }
        }
    }
