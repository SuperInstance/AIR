# AIR

Adaptive Intelligence Runtime — the runtime interface layer between agents and their environment, providing dynamic model loading, adaptive batch sizing, and resource-aware scheduling for the Cocapn fleet.

## Brand Line
> The medium agents breathe through — AIR is the runtime layer that makes fleet intelligence operational.

## Installation

```bash
pip install cocapn-air
```

## Usage

```python
import air

# Initialize runtime
runtime = air.Runtime(
    model="fleet/default",
    adaptive_batching=True,
    resource_policy="auto"
)

# Run inference
result = runtime.execute("Process and route this request")
```

## Fleet Context

Part of the Cocapn fleet. Related repos:
- [JetsonClaw1-vessel](https://github.com/Lucineer/JetsonClaw1-vessel) — edge-native agent case study
- [Equipment-Swarm-Coordinator](https://github.com/SuperInstance/Equipment-Swarm-Coordinator) — multi-agent orchestration
- [Equipment-Consensus-Engine](https://github.com/SuperInstance/Equipment-Consensus-Engine) — multi-agent deliberation
- [plato-sdk](https://github.com/SuperInstance/plato-sdk) — agent communication protocol

🦐 Cocapn fleet — lighthouse keeper architecture
