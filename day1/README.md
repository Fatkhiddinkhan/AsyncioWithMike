# Day 1: Mastering Asyncio basics

## What I Learned Today - `asyncio`

### 🌟 Overview

Today, I took a deep dive into **Python’s ********`asyncio`******** module** and explored various concepts that are crucial for writing efficient asynchronous programs. Below is a **summary of everything I’ve learned**, along with key takeaways and example codes.

---

### ✅ \*\*1. Understanding Coroutines (`async def` & `await`)

\*\*

- **Coroutines** are special Python functions defined using `async def`.
- They allow the program to **pause and resume execution**, making them ideal for handling asynchronous tasks.
- `await` is used inside a coroutine to **pause execution** and let other tasks run.

**Example:**

```python
import asyncio

async def my_coroutine():
    print("Start task")
    await asyncio.sleep(2)
    print("Task finished")

asyncio.run(my_coroutine())
```

---

### ✅ **2. Event Loop (********`asyncio.get_event_loop()`********)**

- The **event loop** is responsible for managing and scheduling coroutines.
- `asyncio.run(coroutine)` is a modern way to **start and close the loop automatically**.
- Alternatively, we can manually get the event loop using `asyncio.get_event_loop()` and control execution with `loop.run_until_complete()`.

**Example:**

```python
loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())
```

---

### ✅ **3. Running Tasks Sequentially vs Concurrently**

#### 🔹 **Sequential Execution (Blocking)**

- Using `await` on coroutines executes them **one at a time**, blocking until each is finished.

```python
async def run_sequential():
    await my_coroutine("Task 1", 2)
    await my_coroutine("Task 2", 3)
```

#### 🔹 **Concurrent Execution (Non-Blocking)**

- Using `asyncio.create_task()` allows tasks to run **simultaneously**.

```python
async def run_concurrent():
    task1 = asyncio.create_task(my_coroutine("Task 1", 2))
    task2 = asyncio.create_task(my_coroutine("Task 2", 3))
    await asyncio.gather(task1, task2)
```

---

### ✅ **4. Monitoring Task Progress**

- **Checking task status** using `task.done()` and retrieving results with `task.result()`.
- \*\*Using \*\***`add_done_callback()`** to execute a function when a task finishes.
- **Processing tasks as they complete** using `asyncio.as_completed()`.

**Example:**

```python
async def fetch_data(task_name, delay):
    await asyncio.sleep(delay)
    return f"{task_name} completed"

def on_task_done(task):
    print(f"Task finished: {task.result()}")

loop = asyncio.get_event_loop()
task = loop.create_task(fetch_data("Task 1", 3))
task.add_done_callback(on_task_done)
loop.run_until_complete(task)
```

---

### ✅ **5. Async Queues (********`asyncio.Queue`********)**

- Used for **producer-consumer patterns** to handle tasks efficiently.
- `queue.put(item)` adds an item to the queue.
- `queue.get()` retrieves an item while waiting for data if necessary.

**Example:**

```python
async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        await queue.put(i)
        print(f"Produced: {i}")

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed: {item}")
        await asyncio.sleep(2)

queue = asyncio.Queue()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(producer(queue), consumer(queue)))
```

---

### **🚀 Summary of Key Takeaways**

| Concept                    | Key Learning                               |
| -------------------------- | ------------------------------------------ |
| `async def` & `await`      | Define and pause coroutines                |
| `asyncio.run()`            | Starts and manages event loop              |
| `asyncio.get_event_loop()` | Manually manage event loop                 |
| `asyncio.create_task()`    | Runs multiple coroutines concurrently      |
| `asyncio.gather()`         | Collects multiple tasks into one execution |
| `asyncio.Queue()`          | Handles producer-consumer workflows        |

---

**This journey is just getting started! 🚀**

---

This README documents my daily learning process. Stay tuned for more updates! 😊

