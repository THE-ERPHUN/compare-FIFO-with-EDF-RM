
# Comparison of FIFO, RM and EDF Scheduling Algorithms

processes = [
    {"pid": "P1", "arrival": 0, "burst": 4, "period": 8, "deadline": 8},
    {"pid": "P2", "arrival": 0, "burst": 2, "period": 5, "deadline": 5},
    {"pid": "P3", "arrival": 0, "burst": 3, "period": 10, "deadline": 10},
]


def simulate(algorithm, processes, total_time=30):
    jobs = []

    for p in processes:
        jobs.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "remaining": p["burst"],
            "period": p["period"],
            "deadline": p["deadline"],
            "order": len(jobs)
        })

    # Generate periodic jobs
    for p in processes:
        t = p["period"]
        while t < total_time:
            jobs.append({
                "pid": p["pid"],
                "arrival": t,
                "burst": p["burst"],
                "remaining": p["burst"],
                "period": p["period"],
                "deadline": t + p["deadline"],
                "order": len(jobs)
            })
            t += p["period"]

    completed = []
    timeline = []
    current = 0

    while current < total_time:
        ready = [
            j for j in jobs
            if j["arrival"] <= current and j["remaining"] > 0
        ]

        if not ready:
            timeline.append("Idle")
            current += 1
            continue

        if algorithm == "FIFO":
            selected = min(ready, key=lambda j: j["order"])

        elif algorithm == "RM":
            selected = min(ready, key=lambda j: j["period"])

        elif algorithm == "EDF":
            selected = min(ready, key=lambda j: j["deadline"])

        selected["remaining"] -= 1
        timeline.append(selected["pid"])
        current += 1

        if selected["remaining"] == 0:
            completion = current
            turnaround = completion - selected["arrival"]
            waiting = turnaround - selected["burst"]

            completed.append({
                "pid": selected["pid"],
                "waiting": waiting,
                "turnaround": turnaround,
                "completion": completion,
                "deadline": selected["deadline"],
                "missed": completion > selected["deadline"]
            })

    return completed, timeline


def compare():
    algorithms = ["FIFO", "RM", "EDF"]

    for algorithm in algorithms:
        results, timeline = simulate(algorithm, processes)

        avg_wait = sum(x["waiting"] for x in results) / len(results)
        avg_turn = sum(x["turnaround"] for x in results) / len(results)
        missed = sum(x["missed"] for x in results)

        print("\nAlgorithm:", algorithm)
        print("-" * 60)

        print("PID\tCT\tWT\tTAT\tDeadline\tMissed")

        for x in results:
            print(
                f'{x["pid"]}\t{x["completion"]}\t'
                f'{x["waiting"]}\t{x["turnaround"]}\t'
                f'{x["deadline"]}\t{x["missed"]}'
            )

        print("Average Waiting Time:", round(avg_wait, 2))
        print("Average Turnaround Time:", round(avg_turn, 2))
        print("Missed Deadlines:", missed)

        print("Gantt Chart:")
        print(" | ".join(timeline))


compare()
