# Comparison of FIFO, RM, and EDF Scheduling Algorithms

## 📌 Overview

This project compares three scheduling algorithms: **First In, First Out (FIFO)**, **Rate Monotonic (RM)**, and **Earliest Deadline First (EDF)**.

The purpose of this project is to analyze how different scheduling strategies execute tasks and how effectively they handle deadlines in real-time systems.

## 🎯 Objectives

- Implement FIFO, RM, and EDF scheduling algorithms.
- Compare task execution order under different scheduling policies.
- Analyze deadline satisfaction and missed deadlines.
- Evaluate CPU utilization and scheduling performance.
- Understand the differences between queue-based, fixed-priority, and dynamic-priority scheduling.

## 🧠 Scheduling Algorithms

### 1. FIFO (First In, First Out)

FIFO executes tasks in the order they enter the ready queue.

**Characteristics:**
- Tasks are processed in arrival order.
- Does not prioritize tasks based on their deadlines or periods.
- Simple to implement and understand.
- Does not generally guarantee that real-time deadlines will be met.

### 2. RM (Rate Monotonic)

RM is a fixed-priority scheduling algorithm designed for periodic real-time tasks.

**Characteristics:**
- Tasks with shorter periods receive higher priorities.
- Priorities remain fixed during execution.
- Commonly analyzed under preemptive scheduling assumptions.
- Provides schedulability guarantees under specific system assumptions.

### 3. EDF (Earliest Deadline First)

EDF is a dynamic-priority scheduling algorithm that selects the ready task with the earliest absolute deadline.

**Characteristics:**
- Tasks with earlier deadlines receive higher priority.
- Priorities may change during execution.
- Dynamically selects tasks according to their deadlines.
- Can achieve up to 100% CPU utilization under ideal uniprocessor scheduling assumptions.

## 📊 Algorithm Comparison

| Feature | FIFO | RM | EDF |
|---|---|---|---|
| Scheduling policy | Arrival order | Fixed priority | Dynamic priority |
| Priority assignment | Queue order | Shorter period = higher priority | Earlier deadline = higher priority |
| Priority changes | No | No | Yes |
| Deadline awareness | No | Indirect | Direct |
| Designed for real-time scheduling | Not specifically | Yes | Yes |
| Theoretical schedulability guarantees | No general guarantee | Yes, under specific assumptions | Yes, under specific assumptions |
| Implementation complexity | Low | Low to moderate | Moderate |

## ⚙️ Task Parameters

The scheduling simulation may use the following parameters to describe each task:

- **Arrival Time (A):** The time at which a task becomes available for execution.
- **Execution Time (C):** The CPU time required to complete a task.
- **Period (T):** The interval between consecutive releases of a periodic task.
- **Deadline (D):** The time by which a task must complete.

The exact parameters depend on the task model used in the implementation.

## 📈 Performance Metrics

The algorithms can be evaluated using the following metrics:

- **CPU Utilization:** The proportion of processor time spent executing tasks.
- **Deadline Misses:** The number of tasks that fail to meet their deadlines.
- **Completion Time:** The time at which a task finishes execution.
- **Waiting Time:** The time a task spends waiting for processor access.
- **Scheduling Order:** The sequence in which tasks are selected for execution.

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### Run the Project

Use the command appropriate for your implementation.

For example, if the project is written in Python:

```bash
python main.py
```

Replace the command with the appropriate execution command if another programming language is used.

## 📁 Project Structure

Example project structure:

```text
.
├── README.md
├── src/
│   └── main.py
├── tests/
└── results/
```

Adapt this structure to match the actual files in your repository.

## 🔬 Expected Results

The comparison aims to demonstrate that:

- FIFO prioritizes task arrival order rather than deadline urgency.
- RM uses fixed priorities based on task periods.
- EDF dynamically prioritizes tasks based on their absolute deadlines.
- The performance of each algorithm depends on task parameters, scheduling assumptions, and implementation details.

Under ideal uniprocessor conditions, EDF can schedule independent preemptive periodic tasks with deadlines equal to their periods whenever total processor utilization does not exceed 100%. RM has a well-known sufficient utilization bound that approaches approximately 69.3% as the number of tasks increases.

These theoretical guarantees do not automatically apply to every implementation or task model.

## 🛠️ Technologies

Update this section according to the technologies used in the project.

- **Programming Language:** [Your Language]
- **Development Environment:** [Your IDE]
- **Version Control:** Git and GitHub

## 👨‍💻 Author

ERPHUN

- GitHub: [@THE-ERPHUN](https://github.com/THE-ERPHUN)

---

If you find this project useful, consider giving the repository a ⭐.

<img width="1661" height="1038" alt="Screenshot 2026-10-18 143945" src="https://github.com/user-attachments/assets/762e0f97-30a0-4323-ad62-14caa946ce8b" />
