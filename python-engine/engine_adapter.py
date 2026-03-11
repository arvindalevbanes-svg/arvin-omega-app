from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import subprocess
import shlex


def _run_command(command: str, cwd: Path | None = None) -> str:
    completed = subprocess.run(
        shlex.split(command),
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
        timeout=300,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip() or "ARVIN command failed")
    return completed.stdout


def run_backtest(dataset_path: str, payout_path: str | None = None) -> Dict[str, Any]:
    """
    TODO:
    Replace this stub with the real ARVIN invocation.
    Example:
        python main.py backtest --data <dataset_path> [--payout <payout_path>]
    """
    command = f"python main.py backtest --data \"{dataset_path}\""
    if payout_path:
        command += f" --payout \"{payout_path}\""

    return {
        "mode": "backtest",
        "dataset": dataset_path,
        "payout": payout_path,
        "commandPreview": command,
        "note": "Stub result. Wire this to your real ARVIN engine.",
        "output": "ARVIN backtest output will appear here once connected."
    }


def run_live(dataset_path: str) -> Dict[str, Any]:
    """
    TODO:
    Replace this stub with your real live-mode invocation.
    """
    command = f"python main.py live --data \"{dataset_path}\""
    return {
        "mode": "live",
        "dataset": dataset_path,
        "commandPreview": command,
        "note": "Stub result. Wire this to your real ARVIN engine.",
        "tickets": [],
        "output": "ARVIN live output will appear here once connected."
    }
