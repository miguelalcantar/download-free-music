# download-free-music
Downloads youtube songs with a bit of web scrapping


How to use it:

Linux:

- Create a virtual environment

move to your working folder and with the command line:
virtualenv .

- Use virtualenv

source bin/activate

- Install required libraries

pip install youtube_dl, bs4, selenium

- Create a music file. Its format is the following
Recommended, after all is going to be the query on youtube so
even if it is wrong youtube will fix it ;)

group of music - song

example:

Joy Division - Leave Me Alone

so, in the command line:

cat > music.txt
<<here goes all your songs>>

-Finally download the music:

python download-music.py
