from setuptools import setup

setup(
	name="subtle",
	version="1.0.0",
	py_modules=['subtle'],
	install_requires=[
		'click',
		'colorama',
		'peewee'
	],
	entry_points='''
		[console_scripts]
		subtle=subtle.__init__:cli
		''',
	)