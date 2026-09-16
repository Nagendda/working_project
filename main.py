"""
Dynamic Knowledge Allocation for Continual Learning
====================================================
Main entry point.

Usage
-----
    python main.py --config configs/base_config.yaml [--dry-run]

Flags
-----
--config PATH   Path to a YAML configuration file (required).
--dry-run       Load config and print a summary, then exit without training.
--task INT      Run a specific task index only (0-based). Default: all tasks.
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Dynamic Knowledge Allocation for Continual Learning"
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/base_config.yaml"),
        help="Path to YAML configuration file.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Load config, print summary, then exit.",
    )
    parser.add_argument(
        "--task",
        type=int,
        default=None,
        help="(Optional) Run only the specified task index (0-based).",
    )
    return parser.parse_args()


def _setup_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main() -> int:
    """
    Main orchestration entry point.

    Phase 0: scaffold only — loads config and exits with a summary.
    Later phases will add the full training loop here.
    """
    args = _parse_args()

    # ── Config loading (placeholder until Phase 1) ──────────────────────────
    # Import lazily to avoid hard dependency during basic Python checks.
    try:
        import yaml  # type: ignore[import]

        with open(args.config, "r", encoding="utf-8") as fh:
            cfg = yaml.safe_load(fh)
    except FileNotFoundError:
        print(f"[ERROR] Config file not found: {args.config}", file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover
        print(f"[ERROR] Failed to load config: {exc}", file=sys.stderr)
        return 1

    _setup_logging(cfg.get("logging", {}).get("level", "INFO"))
    log = logging.getLogger(__name__)

    log.info("=" * 60)
    log.info("Dynamic Knowledge Allocation for Continual Learning")
    log.info("=" * 60)
    log.info("Project  : %s", cfg["project"]["name"])
    log.info("Version  : %s", cfg["project"]["version"])
    log.info("Phase    : %s", cfg["project"]["phase"])
    log.info("Config   : %s", args.config)

    task_stream_cfg = cfg.get("task_stream", {})
    log.info(
        "Tasks    : %d tasks × %d classes",
        task_stream_cfg.get("num_tasks", "?"),
        task_stream_cfg.get("classes_per_task", "?"),
    )

    if args.dry_run:
        log.info("Dry-run mode — exiting without training.")
        return 0

    # ── Future phases will plug in here ────────────────────────────────────
    log.warning(
        "Training loop not yet implemented (Phase 0 — scaffold only). "
        "Use --dry-run to verify the configuration."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
