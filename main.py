import sys

from generators.detector import (
    detect_project
)

from generators.docker_generator import (
    generate_dockerfile
)
from generators.compose_generator import (
    generate_compose
)

project_path = sys.argv[1]

info = detect_project(
    project_path
)

print("\nProject Detection")

print(
    f"Framework : {info['framework']}"
)

print(
    f"Entrypoint : {info['entrypoint']}"
)

print(
    f"Port       : {info['port']}"
)

generate_dockerfile(
    project_path=project_path,
    entrypoint=info["entrypoint"],
    port=info["port"]
)

service_name = (
    project_path
    .replace("\\", "-")
    .replace("/", "-")
    .split("-")[-1]
)

generate_compose(
    project_path=project_path,
    service_name=service_name,
    port=info["port"]
)