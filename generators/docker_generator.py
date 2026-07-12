from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def generate_dockerfile(
    project_path,
    entrypoint="app.py",
    port=8000
):

    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template(
        "Dockerfile.j2"
    )

    content = template.render(
        entrypoint=entrypoint,
        port=port
    )

    output = Path(project_path) / "Dockerfile"

    output.write_text(content)

    print("Dockerfile generated")