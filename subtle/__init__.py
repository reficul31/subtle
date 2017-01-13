from .models import db, Point, initdb
import click
import os

@click.group()
def create():
	pass

@create.command()
@click.argument('title')
def checkpoint(title):
	print("Making a new checkpoint")
	point = Point.create(title = title, dir=os.getcwd())

@create.command()
def list():
	points = Point.select()
	for point in points:
		print(point.title +" : "+ point.dir)

@create.command()
def dbinit():
	initdb()

@click.group()
def start():
	pass

@start.command()
@click.argument('title')
def open(title):
	point = Point.get(Point.title == title)
	os.system('subl %s'%point.dir)

@click.group()
def delete():
	pass

@delete.command()
@click.argument('title')
def destroy(title):
	print("Destroying the checkpoint %s"%title)
	point = Point.get(Point.title == title)
	point.delete_instance()

main = click.CommandCollection(sources=[create,start, delete])

if __name__ == '__main__':
	cli