# Dynamic Knowledge Allocation for Continual Learning

> **Research Prototype** — investigating whether a neural model can continuously
> learn a stream of new information with very few parameter updates while
> preserving old knowledge through a **dynamic knowledge-allocation policy**
> under fixed parameter and memory budgets.

---

## Research Question

> *"Can a neural model continuously learn a stream of new information using a
> very small number of parameter updates while preserving old knowledge through
> dynamic knowledge allocation?"*

---

## Research Position

The following techniques are individually **established**:

| Technique | Status |
|---|---|
| Continual Learning | Established |
| LoRA / Adapters | Established |
| Replay Memory | Established |
| External Vector Memory | Established |
| Dynamic Routing | Established |
| Machine Unlearning | Established |
| Knowledge Distillation | Established |

**The potential novel contribution** is the *interaction* of these components
through a **dynamic knowledge-allocation policy** under joint fixed parameter and
memory budgets — a system-level contribution rather than a component-level one.

---

## Architecture

```
Continuous Data
      ↓
Frozen Foundation Model
      ↓
Feature Encoder
      ↓
Feature Vector
      ↓
Memory Retrieval
      ↓
Memory Judge
      ↓
Knowledge Allocation
      ↓
┌──────────────┬──────────────┬──────────────┐
│  PRESERVE    │  STRENGTHEN  │    STORE     │
│              │              │              │
│ LoRA/Adapter │ LoRA/Adapter │  External    │
│              │              │  Memory      │
└──────────────┴──────────────┴──────────────┘
      ↓
Replay + Prediction
      ↓
Memory State Update
      ↓
Strengthening / Weakening
      ↓
Archive
      ↓
Recovery
```

---

## Repository Layout

```
dynamic-memory-ai/
│
├── .agents/skills/          # Agent skill definitions
├── configs/                 # YAML configuration files
├── data/                    # Dataset loaders and preprocessing
├── models/                  # Foundation model wrappers, LoRA, adapters
├── memory/                  # External vector store, memory judge, archive
├── continual/               # Task stream, allocation policy, trainer
├── evaluation/              # Metrics, forgetting curves, analysis
├── experiments/             # Experiment launch scripts
├── scripts/                 # Setup, data download, Colab bootstrap
├── tests/                   # pytest test suite
├── notebooks/               # Exploratory Jupyter notebooks
├── results/                 # Saved metrics and plots (git-ignored)
├── checkpoints/             # Model checkpoints (git-ignored)
├── docs/                    # Extended design documents
├── requirements.txt
├── README.md
├── AGENTS.md
├── .gitignore
└── main.py
```

---

## Quick Start

### 1 — Install dependencies

```bash
pip install -r requirements.txt
```

### 2 — Verify installation (CPU smoke test)

```bash
python main.py --config configs/base_config.yaml --dry-run
```

### 3 — Run tests

```bash
pytest tests/ -v
```

---

## Dataset: CIFAR-100 (Class-Incremental)

| Task | Classes |
|------|---------|
| Task 1 | 0 – 19 |
| Task 2 | 20 – 39 |
| Task 3 | 40 – 59 |
| Task 4 | 60 – 79 |
| Task 5 | 80 – 99 |

**Anti-leakage guarantee:** the task stream enforces strict ordering;
future-task classes are never exposed during training.

---

## Compute

| Environment | Hardware | Notes |
|---|---|---|
| Local dev | CPU (Windows) | Smoke tests only |
| Training | Google Colab T4 | 16 GB VRAM, single GPU |

---

## Development Rules

1. Code must run locally for CPU smoke tests.
2. Training code targets a single T4 GPU.
3. No hard-coded machine-specific paths.
4. YAML configuration files for all hyperparameters.
5. Relative paths wherever possible.
6. Automatic CUDA detection.
7. Mixed-precision (AMP) support.
8. Gradient accumulation support.
9. T4-safe memory usage.
10. Never fabricate experiment results.
11. Never silently change dataset splits.
12. No future-task class leakage.
13. Always report total and trainable parameter counts.
14. Baseline and proposed implementations are kept separate.
15. Tests must pass before moving to the next development phase.

---

## Development Phases

- [x] **Phase 0** — Repository scaffold, configs, placeholder modules, tests
- [ ] **Phase 1** — Foundation model + feature encoder
- [ ] **Phase 2** — External memory (FAISS + SQLite)
- [ ] **Phase 3** — Memory judge + knowledge allocation policy
- [ ] **Phase 4** — LoRA / adapter modules (preserve / strengthen)
- [ ] **Phase 5** — Continual training loop + replay
- [ ] **Phase 6** — Evaluation harness (forgetting, transfer, BWT, FWT)
- [ ] **Phase 7** — Baseline comparisons
- [ ] **Phase 8** — Analysis, ablations, write-up

---

## License

Research prototype — license to be decided.
