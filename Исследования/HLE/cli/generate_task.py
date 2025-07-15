import json
import sys

with open("datasets/hle_test_sample.jsonl", "r") as f:
    input_data = [json.loads(line) for line in f]

task = {
    "task_id": "hle_phi_001",
    "instruction": "Сгенерировать логический ответ на каждый вопрос. Указать reasoning_steps и оценить когерентность (Tₓ).",
    "input": input_data,
    "constraints": {
        "trap_threshold": 0.02,
        "max_steps": 10
    }
}

with open("tasks/task_hle_phi_eval.json", "w") as out:
    json.dump(task, out, indent=2)

print("✅ Задание сгенерировано: tasks/task_hle_phi_eval.json")
