**Topics:** `adaptive-runtime` `inference` `model-loading` `batching` `resource-scheduling` `fleet-layer` `cocapn`

---

# AIR — Adaptive Intelligence Runtime

> The medium agents breathe through — AIR is the runtime layer that makes fleet intelligence operational.

**AIR** (Adaptive Intelligence Runtime) is the **runtime interface layer** between AI agents and their compute environment. It provides dynamic model loading, adaptive batch sizing, and resource-aware scheduling — so agents can focus on thinking, not managing hardware.

Part of the [Cocapn fleet](https://github.com/SuperInstance) — lighthouse keeper architecture.

---

## What It Does

AIR sits between the agent and the hardware. When an agent needs to run inference, AIR handles:

- **Dynamic model loading** — Load models on-demand, hot-swap between model sizes based on task complexity
- **Adaptive batch sizing** — Group requests into batches sized to the available GPU memory (small for RTX 4050, large for A100)
- **Resource-aware scheduling** — Route based on device capability, current load, and budget constraints

Think of it as the **air traffic control tower** for inference requests. Every agent submits its request; AIR routes it to the right runway.

---

## Quick Start

### Install

```bash
pip install cocapn-air
```

### Basic Usage

```python
import air

# Initialize the runtime
runtime = air.Runtime(
    model="fleet/default",           # Model path or registry ID
    adaptive_batching=True,         # Dynamically size batches
    resource_policy="auto"          # Let AIR decide based on device
)

# Execute inference
result = runtime.execute("What is the current fleet status?")

print(f"Response: {result['text']}")
print(f"Model: {result['model']}")
print(f"Latency: {result['latency_ms']}ms")
print(f"Batch size: {result['batch_size']}")
```

### Configuration Options

```python
runtime = air.Runtime(
    model="glm-5.1",               # Specific model
    adaptive_batching=True,        # True = auto-size batches
    batch_size=8,                  # Fixed batch size (overrides adaptive)
    resource_policy="jetson",       # Target device: "auto" | "jetson" | "cloud" | "cpu"
    max_tokens=2048,               # Generation limit
    temperature=0.7,               # Sampling temperature
)
```

---

## Architecture

```
AIR/
├── README.md
├── CHARTER.md
├── DOCKSIDE-EXAM.md
├── LICENSE
└── tests/
    └── test_air_docs.py          # Documentation contract tests
```

### Component Overview

| Component | Role |
|-----------|------|
| `Runtime` | Main entry point. Initializes models, manages batching, routes requests |
| Model Loader | Loads and hot-swaps models based on device capability |
| Batch Scheduler | Groups concurrent requests into GPU-efficient batches |
| Resource Monitor | Tracks GPU memory, CPU load, latency percentiles |

### Decision Flow

```
Agent Request
    │
    ▼
Batch Scheduler ──are there other pending requests?── Yes ──► Group into batch
    │                                                        │
    │ No                                                     ▼
    ▼                                                   Execute on GPU
Resource Monitor                                          │
    │                                                        ▼
    ▼                                                   Unbundle results
Return Result ───────────────────────────────────────────► Agent
```

---

## Demo: Simulated Runtime

Since AIR is documented-first (code is implementation in progress), here's a **simulated demo** showing the expected API:

```python
import air

# Simulate the runtime behavior
runtime = air.Runtime(
    model="fleet/default",
    adaptive_batching=True,
    resource_policy="auto"
)

# Example: Fleet status check
result = runtime.execute("Check fleet health")
# Expected output:
# {
#   'text': 'Fleet is healthy. 12 agents active, 2 services down.',
#   'model': 'glm-5.1',
#   'latency_ms': 234,
#   'batch_size': 3,
#   'device': 'jetson-orin'
# }

# Example: Complex reasoning task
result = runtime.execute("Design a routing algorithm for fleet orchestration")
# {
#   'text': '[detailed response...]',
#   'model': 'glm-5.1',
#   'latency_ms': 1247,
#   'batch_size': 1,
#   'device': 'cloud-a100'
# }
```

---

## Fleet Context

Part of the Cocapn fleet. Related repos:

| Repo | Role |
|------|-------|
| [JetsonClaw1-vessel](https://github.com/Lucineer/JetsonClaw1-vessel) | Edge-native agent case study |
| [Equipment-Swarm-Coordinator](https://github.com/SuperInstance/Equipment-Swarm-Coordinator) | Multi-agent orchestration |
| [Equipment-Consensus-Engine](https://github.com/SuperInstance/Equipment-Consensus-Engine) | Multi-agent deliberation |
| [plato-sdk](https://github.com/SuperInstance/plato-sdk) | Agent communication protocol |
| [cudaclaw](https://github.com/SuperInstance/cudaclaw) | GPU-accelerated agent orchestration |

---

## Status

AIR is in **Active** development. The README and documentation describe the intended API; the implementation follows the spec in `DOCKSIDE-EXAM.md`.

For implementation status, see `STATE.md` (if present) or check the [fleet-status](https://github.com/SuperInstance/fleet-status) live endpoints.

---
🦐 Cocapn fleet — lighthouse keeper architecture
