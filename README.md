# Python Network Programming 2025

A weekly lab-based journey from classical sockets to future networks. Building one network agreement in Python every week—simple first, then fragile, then strange.

## Course Philosophy

Networks are not cables and boxes. **They are agreements under uncertainty.** You already know IP addressing and routing. Now we program behavior.

## Learning Path Overview

| Week | Topic | Type | Core Concepts |
|------|-------|------|---|
| 1 | Client–Server Communication (TCP Unicast) | BASIC | TCP sockets, bind, listen, accept, connect, request–response |
| 2 | UDP Communication (Connectionless Unicast) | BASIC | UDP sockets, datagrams, packet loss, no guarantees |
| 3 | Broadcast Communication | BASIC | LAN broadcast scope, discovery, service advertisement |
| 4 | Multicast Communication | BASIC | Group membership, multicast groups, selective delivery |
| 5 | Peer-to-Peer Networking | BASIC | Symmetric roles, dynamic ports, no central server |
| 6 | Ad-Hoc Networking (MANET Simulation) | BASIC | Neighbor discovery, routing, TTL, improvised networks |
| 7 | Store-and-Forward Communication | BASIC | Message queues, retry logic, persistent buffers |
| 8 | Opportunistic Routing | ADVANCED | Probability-based forwarding, encounter routing |
| 9 | Bio-Inspired Networking | ADVANCED | Pheromone routing, reinforcement learning, adaptive paths |
| 10 | Quantum-Inspired Networking | ADVANCED | No-cloning, one-time tokens, quantum-secure concepts |

## 📋 Kanban: Implementation Checklist

### ✅ Completed Implementations
- [x] Week 1: TCP Client–Server (server.py, server_threaded.py, client.py)
- [x] Week 2: UDP Unicast (sender.py, receiver.py)
- [x] Week 3: UDP Broadcast (broadcaster.py, listener.py)
- [x] Week 4: UDP Multicast (sender.py, receiver.py)
- [x] Week 5: Peer-to-Peer (peer.py)
- [x] Week 6: MANET Phase-1 (node.py with random port support)
- [x] Week 7: Store-and-Forward Phase-1 (node.py, message_queue.py)
- [x] Week 8: Opportunistic Routing Implementation (node.py, delivery_table.py)
- [x] Week 9: Bio-Inspired Networking (node.py, pheromone_table.py)
- [x] Week 10: Quantum-Inspired Networking (node.py, token.py)

### 🚧 In Progress / Planning
- [ ] Portfolio Integration & Final Review

### 📦 Codebase Structure

```text
networkprogramming2025/
├── week01-tcp-client-server-basic/
├── week02-udp-unicast-basic/
├── week03-udp-broadcast-basic/
├── week04-udp-multicast-basic/
├── week05-peer-to-peer-basic/
├── week06-manet-basic/
├── week07-store-forward-basic/
├── week08-opportunistic-routing-basic/
│   ├── node.py
│   ├── delivery_table.py
│   └── config.py
├── week09-bio-routing-basic/
│   ├── node.py
│   ├── pheromone_table.py
│   └── config.py
├── week10-quantum-network-basic/
│   ├── node.py
│   ├── token.py
│   └── config.py
└── workshop/
    ├── Curriculum- Network Programming 2025.md
    └── [Lab guides and research notes]
```
## Key Learning Outcomes by Week

### WEEK 1 – TCP Unicast
- Understand TCP client–server architecture
- Implement blocking socket communication
- Relate TCP reliability to application behavior
- **Traits**: Structured thinking, protocol discipline

### WEEK 2 – UDP Unicast
- Compare TCP vs UDP trade-offs
- Implement connectionless communication
- Observe and handle packet loss behavior
- **Traits**: Risk awareness, performance analysis

### WEEK 3 – Broadcast
- Understand LAN broadcast scope
- Implement discovery mechanisms
- **Real-world usage**: DHCP, service discovery

### WEEK 4 – Multicast
- Join multicast groups
- Differentiate multicast vs broadcast
- Opt-in group communication
- **Real-world usage**: Video streaming, pub/sub

### WEEK 5 – Peer-to-Peer
- Build symmetric network roles
- Handle dynamic ports
- **Real-world usage**: File sharing, decentralized systems

### WEEK 6 – Ad-Hoc Networking (MANET)
- Simulate neighbor discovery
- Implement forwarding with TTL
- **Extension**: AODV/OLSR concepts

### WEEK 7 – Store-and-Forward
- Implement message queues
- Handle retry logic
- **Extension**: Persistent storage, delay-tolerant networks

### WEEK 8 – Opportunistic Routing (Advanced)
- Maintain delivery probability metrics per neighbor
- Forward packets opportunistically based on these probabilities
- **Real-world usage**: Delay-Tolerant Networks, Wildlife Tracking
- **Traits**: Probabilistic reasoning, Adaptive decision-making

### WEEK 9 – Bio-Inspired Networking (Advanced)
- Implement reinforcement-inspired routing decisions
- Maintain adaptive pheromone tables (Reinforcement & Decay)
- **Real-world usage**: Dynamic IoT routing, Self-healing networks
- **Traits**: Self-optimizing systems, Reinforcement reasoning

### WEEK 10 – Quantum-Inspired Networking (Advanced)
- Implement one-time-read message tokens
- Model network state collapse upon access
- **Real-world usage**: Secure ephemeral messaging, QKD concepts
- **Traits**: Security-conscious thinking, Conceptual modeling

## Getting Started

1. Navigate to any `week*` directory
2. Configure your environment in `config.py`
3. Run server/sender in one terminal
4. Run client/receiver in another terminal
5. Observe the network behavior

Example (Week 8-10):
```bash
python node.py

Current Status: Weeks 1-10 fully implemented with all core functionality and advanced concepts successfully tested. Ready for portfolio showcase!