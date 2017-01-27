# subtle
A small CLI to make checkpoints in files and open them in sublime faster.(for Linux)

## Why this plugin?
Well i used to get very frustrated everytime I wanted to open a sublime folder i had to go in the sublime window click on the File > Open Folder and then select my file from the file explorer.  
So well this plugin makes it a bit easier to navigate through the directory and add files that we like to switch constantly.

## Prerequisites
> Sublime text editor  
> Python

## How to install?
* First clone the repository ```git clone https://github.com/reficul31/subtle```
* When inside the repository open the virtualenv in which you want to work in or install in root.
* Open the terminal and run ```pip install .```
* For development run ```pip install --editable .```
* You are ready!

## Usage
##### Before using
Before using the plugin it is imperitive that you run the command  
```subtle dbinit```  
This will initialize the database to store the checkpoints in.

##### Help
Any help regarding the usage of the plugin can be found by typing the command  
```subtle --help```  
Thanks to our friends at [Click](https://github.com/pallets/click) the plugin cam with a lot of out of the box help setup. Check them out they are awesome.

##### Making a checkpoint
* Making a checkpoint in the current directory.  
```subtle checkpoint [name-of-checkpoint]```
* Making a checkpoint in remote directory.  
```subtle checkpoint [name-of-checkpoint] --dirname [path-to-dir]```
* Any help on using the checkpoint command can be found by typing  
```subtle checkpoint --help```

##### Deleting a checkpoint
To delete a checkpoint  
```subtle destroy [name-of-checkpoint]```

##### Listing out all the checkpoints
To list out all the checkpoint that were made  
```subtle list```

##### Opening the checkpoint
* To open a checkpoint  
```subtle open [name-of-checkpoint]```
* To open a file using subtle  
```subtle open --file [name-of-file]```
* To open a folder without making a checkpoint  
```subtle open --folder [path-to-folder]```

##### Contribution
Send pull request as frequently as you want. If it builds, possibility is, it will get merged. We love pull requests. I know the plugin is a bit rough around the edges but if you can do it better send me a pull request.

### TODOS
- [ ] @todo remove peewee dependency
- [ ] @todo better error handling
- [ ] @todo adding autocompletion  
- [ ] @todo maybe add change directory option(might be unrealistic)