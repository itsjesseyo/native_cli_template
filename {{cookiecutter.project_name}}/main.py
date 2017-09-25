import sys, json
import click
import py

from config import pass_config

@click.group()
@pass_config
def cli(config):
	config.load()

@cli.command()
@pass_config
def say_hello(config):
	"""say hello to someone"""
	click.echo("Hello, %s" % config.get("name", "unnamed entity"))

@cli.command()
@click.argument('name')
@pass_config
def my_name_is(config, name):
	"""set the name to say hello to"""
	config['name'] = name
	config.save()
	click.echo("Set name")

if __name__ == '__main__':
	cli()