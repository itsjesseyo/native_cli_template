import sys, json
import click
import py

class Config(dict):
	def __init__(self, *args, **kwargs):
		self.config = py.path.local(
			click.get_app_dir('my_app')
		).join('config.json') # A
		# print(click.get_app_dir('my_app'))
		super(Config, self).__init__(*args, **kwargs)
		
	def load(self):
		"""load a JSON config file from disk"""
		try:
			self.update(json.loads(self.config.read())) # B
		except py.error.ENOENT:
			pass
			
	def save(self):
		self.config.ensure()
		with self.config.open('w') as f: # B
			f.write(json.dumps(self))

pass_config = click.make_pass_decorator(Config, ensure=True)