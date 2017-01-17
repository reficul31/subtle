from .models import db, Point, initdb
import click
import os
from colorama import init, Fore, Back, Style
@click.group()
def create():
	pass

@create.command()
@click.argument('title')
@click.option('--dirname', default=os.getcwd(), help='Give a directory name with the tag')
def checkpoint(title, dirname):
	""" Used for saving the checkpoints in the file directory system """
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
	""" Used for listing all the saved checkpoints """
	points = Point.select()
	print(Fore.GREEN+"Checkpoints Found:%s"%Point.select().count())
	for point in points:
		print(Fore.WHITE+point.title +"\t"+ point.dir)

@create.command()
def dbinit():
	""" Used for intializing the database or dropping the current database and making a new one """
	initdb()

@click.group()
def start():
	pass

@start.command()
@click.argument('title', nargs=-1)
@click.option('--file', default=None, help='Give a file path')
@click.option('--folder', default=None, help='Give a folder path')
def open(title, file, folder):
	""" Used to open the files in checkpoints, in directory or even files """
	print("Getting the files...")
	for t in title:
		try:
			point = Point.get(Point.title == t)
			os.system('subl %s'%point.dir)	
		except Exception:
			print(Fore.RED+"Checkpoint %s doesn't exists"%t)
	if file:
		if os.path.isfile(file):
			os.system('subl %s'%file)
		else:
			print(Fore.RED+"File doesn't exist")
	if folder:
		if os.path.isdir(folder):
			os.system('subl %s'%folder)
		else:
			print(Fore.RED+"Folder doesn't exist")

@click.group()
def delete():
	pass

@delete.command()
@click.argument('title', nargs=-1)
def destroy(title):
	""" Used to destroy the already made checkpoints """
	print("Getting the checkpoints...")
	for t in title:
		try:
			point = Point.get(Point.title == t)
			point.delete_instance()
			print(Fore.GREEN+"Checkpoint %s destroyed successfully"%t+Fore.WHITE)
		except Exception:
			print(Fore.RED+"Checkpoint %s doesn't exist"%t+Fore.WHITE)

main = click.CommandCollection(sources=[create,start, delete])

if __name__ == '__main__':
	init()
	cli