"""Click application to convert json to yaml and yaml to json."""
import json
import yaml
import click

from .utils import parse_as_json, parse_as_yaml


@click.command()
@click.option(
    "-f",
    "--file",
    type=click.File("r"),
    help="The file to open and convert. If not set then defaults to stdin.",
)
@click.option(
    "-o",
    "--output",
    type=click.File("w"),
    help="The destination to write output. If not set then defaults to stdout.",
)
@click.option(
    "-j",
    "--json",
    "file_type",
    flag_value="json",
    default=True,
    help="Flag for json input (Default).",
)
@click.option(
    "-y", "--yaml", "file_type", flag_value="yaml", help="Flag for yaml input."
)
def convert(file_type, file, output):
    """Convert json to yaml and yaml to json.
    Reads from standard in or from a specified file.
    Outputs to standard out or to a specified file.
    """
    if file:
        data = file.read()
    else:
        data = click.get_text_stream("stdin").read().strip()

    if file_type == "json":
        data = parse_as_json(data)
        result = yaml.dump(data)
    else:
        data = parse_as_yaml(data)
        result = json.dumps(data, indent=True)

    if output:
        output.write(result)
    else:
        click.echo(result)
