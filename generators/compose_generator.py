from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def generate_compose(
    project_path,
    service_name,
    port
):

    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template(
        "docker-compose.yml.j2"
    )

    content = template.render(
        service_name=service_name,
        port=port
    )

    output = (
        Path(project_path)
        / "docker-compose.yml"
    )

    output.write_text(content)

    print(
        "docker-compose.yml generated"
    )