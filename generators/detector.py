from pathlib import Path
import re


def detect_project(project_path):

    project_path = Path(project_path)

    framework = None
    entrypoint = None
    port = 8000

    py_files = project_path.glob("*.py")

    for file in py_files:

        content = file.read_text(
            encoding="utf-8"
        )

        if "from flask import" in content:
            framework = "Flask"
            entrypoint = file.name

        elif "from fastapi import" in content:
            framework = "FastAPI"
            entrypoint = file.name

        match = re.search(
            r"port\s*=\s*(\d+)",
            content
        )

        if match:
            port = int(match.group(1))

    return {
        "framework": framework,
        "entrypoint": entrypoint,
        "port": port
    }