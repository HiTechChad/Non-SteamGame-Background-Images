# Non-SteamGame-Background-Images
Program adds background images to non steam games added to library using screenshots
## Requirements
python 2.7
## Setup
1. Add your non steam games into your steam library
2. launch each game and check if steam overlay is enabled. (this will not work without steamoverlay)
3. Using f12 key take the exact amount of screenshots of the number of photos you want to replace them with
4.: locate your steam id number, it can be found at `C:\Program Files (x86)\Steam\userdata` and there will be a folder titled with a large number. COPY THAT NUMBER!!
5. Open config.json and paste the number coppied in the previous step where it says to paste it. Dont forget to save the file.
6. Open a command window and install dependencys using `pip install -r requirements.txt`
7. Create a new folder and place all of your images that you want to replace your screenshots with (ONLY USE JPG IMAGES THE PROGRAM WILL CRASH OTHERWISE).
## How to run the program
1. Open a new command window or use the one priviously opened one from step 6 of setup and run the command `python run.py`.
2. You'll be prompted to enter a game id. This can be found by opening the screenshot library in steam, clicking on "show on disk". Within the file path you should notice a number larger than your steam id, this is the game id. copy that value and enter it into the command line.
3. Next you will be asked if you have preformed step 7 in setup.
4. Enter the name of the folder you created.
5. Wait for program to finnish. It will automaticly replace the screenshots with the correctly named and formated pictures.
