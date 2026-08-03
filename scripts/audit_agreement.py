#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

REQUIRED = ["quality", "communication", "grounding", "completion", "approval", "memory"]
SENSITIVE = {
    "credential": re.compile(r"(?i)(api[_ -]?key|oauth[_ -]?token|password|secret)\s*[:=]\s*\S+"),
    "private IPv4": re.compile(r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"),
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "absolute home path": re.compile(r"/home/[A-Za-z0-9._-]+/"),
}

def audit(text: str) -> list[str]:
    lower = text.lower(); findings = []
    for term in REQUIRED:
        if term not in lower: findings.append(f"missing operating concern: {term}")
    for label, pattern in SENSITIVE.items():
        for match in pattern.finditer(text): findings.append(f"possible {label}: {match.group(0)[:80]}")
    return findings

def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("file"); args = p.parse_args()
    findings = audit(Path(args.file).read_text())
    for item in findings: print(f"FINDING: {item}")
    print("RESULT: PASS" if not findings else "RESULT: REVIEW")
    return 0 if not findings else 1

if __name__ == "__main__": raise SystemExit(main())
