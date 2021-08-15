![Graze Logo](https://github.com/Dungeonation/graze/blob/main/grazelogo.png)  
*Rewrites Scratch projects as GameMaker 1.4 projects*  
  
**Graze** is a *Python* program that parses an unzipped .sb2 Scratch project file, and rewrites the project as a GameMaker 1.4 project. With this, you can free your games and software from Scratch and leverage the power of GameMaker Studio 1.4, which can then be converted to GameMaker Studio 2 if need be. Use GameMaker's exporting capabilities, improve performance, add save data to games, or add Medals or Highscores in web game form using something like the [*Newgrounds.io API*](https://www.newgrounds.io/). 

Only Scratch 2.0 projects are supported right now but Scratch 3.0 support is possible as it's just a different .json format, and will happen in the future.

*Contributing to or testing the tool in its current in-development state requires **Python 3.8** or greater. As of this version of Graze you will also need these Python libraries:*  
* json
* PIL
* pathlib

# Project Status
As of the GitHub release in *August 2021* Graze can only convert over sprites and sounds and establishing variables, and is in the beginning stages of converting code. Check **changelog.txt** frequently as development continues. **To check to see if your Scratch project is compatible**, also check **compatibilitystatus.txt** for the status of Scratch block support in Graze.

# Using Graze

First off, [download Python](https://www.python.org/) and make sure you have the libraries needed installed from the command line ([Here's how to do that](https://docs.python.org/3/installing/index.html) if you're a novice). You'll also need GameMaker Studio 1.4 or higher of course.  
Now download this repository and put it all in its own folder so you don't screw up any of your other files (this tool uses file manipulation, moving, deleting, etc). *In Graze's early stage, check for updates here!*  
A fresh download has the empty GameMaker project folder unzipped in the main folder which Graze will refer to. But for *future conversions*, delete or move that project folder, and within the **blank gamemaker template** folder, unzip the .zip into the main folder.
###### GrazeConvert.py  
Running this in Python immediately begins the conversion process, and runs until finished or encountering an error, then prompting you to press any key to halt the program. *Don't run it if you're not ready!*  
If you run it in the command line instead of within the Python shell, and instead of an error handler in the code itself it just crashes - it'll just close instead of telling you I think. Run it in the Python shell to get a crash report.
###### scratchproject  
This folder is what Graze refers to for the unzipped Scratch project that you wish to convert. Take your Scratch 2.0 (.sb2) file and change the file extension to *.zip* (dunno how to do that? Look up how to show file extensions in file names in your version of Windows or whatever, then you can type in a new file extension when renaming the file. Ignore warnings from doing so), then unzip it into the *scratchproject* folder. Everything in that folder should just be your unzipped Scratch project for conversion, and also keep a backup of the original .sb2 file!!
###### FinishedGame.gmx
The GameMaker project folder Graze works with. It can't just be any old GameMaker project 'cuz this one has unique scripts in it and is also already in the frame rate and screen size of a Scratch project.
###### blank gamemaker template
I just have this here for unzipping a blank copy of the GameMaker project into the main folder for a new conversion.

# License
Graze is licensed under the *GNU General Public License v3.0*. GameMaker is copyright Yoyo Games. Scratch has stated Scratch projects are under the *[Creative Commons Attribution-ShareAlike license](https://creativecommons.org/licenses/by-sa/2.0/deed.en)*, and making a Scratch project and converting it to GameMaker with Graze both allow you to sell your finished project, or distribute it places as you wish. :)

# Contribution

Contributions from everyone are welcome! Any contribution submitted for inclusion in Graze consents to being included and being under the same license as Graze.  
An unzipped *.sb2* file is all the sprites and sounds the Scratch project uses numbered, as well as the all-important **project.json** which contains all the information on the project and its code.  
Scratch has us covered on documentation on the .sb2 file format and its .json, that can be found [here](https://en.scratch-wiki.info/wiki/Scratch_File_Format_(2.0)).  
The goal of Graze is to mimic the behavior of the original Scratch project as *close* as possible in GameMaker without undesired behavior after conversion. Some functions of Scratch such as Extensions other than Pen and Cloud Variables, will not be able to be supported in Graze.
