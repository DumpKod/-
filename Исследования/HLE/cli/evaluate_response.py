import json

with open("agent_io/answers_received.json") as f:
    data = json.load(f)

results = []

for resp in data.get("responses", []):
    result = {
        "question_id": resp["question_id"],
        "Tₓ": resp["Tₓ"],
        "is_coherent": resp["Tₓ"] >= 0.85
    }
    results.append(result)

with open("results/evaluation_log.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Оценка завершена: results/evaluation_log.json")
