from .models import db, Point, initdb
import click
import os
from colorama import init, Fore, Back, Style
@click.group()
def create():
	pass

@create.command()
@click.argument('title')
@click.option('--dirname', default=os.getcwd())
def checkpoint(title, dirname):
	if os.path.isdir(dirname):
		print("Making a new checkpoint....")
		if Point.select().where(Point.title == title).exists() or Point.select().where(Point.dir == dirname).exists():
			print(Fore.RED+"Checkpoint already exists")
		else:
			point = Point.create(title = title, dir=dirname)
			print(Fore.GREEN+"Checkpoint made successully")
	else:
		print(Fore.RED+"Directory doesn't exist"+Fore.WHITE)

@create.command()
def list():
	points = Point.select()
	print(Fore.GREEN+"Checkpoints Found:%s"%Point.select().count())
	for point in points:
		print(Fore.WHITE+point.title +"\t"+ point.dir)

@create.command()
def dbinit():
	initdb()

@click.group()
def start():
	pass

@start.command()
@click.argument('title')
def open(title):
	print("Getting the files")
	point = Point.get(Point.title == title)
	os.system('subl %s'%point.dir)
	print("Opening the folder ...")

@click.group()
def delete():
	pass

@delete.command()
@click.argument('title')
def destroy(title):
	print("Destroying the checkpoint %s"%title)
	point = Point.get(Point.title == title)
	point.delete_instance()
	print(Fore.GREEN+"Checkpoint destroyed successfully")
	print(Fore.WHITE)

main = click.CommandCollection(sources=[create,start, delete])

if __name__ == '__main__':
	init()
	cli