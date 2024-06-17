# import library

from pytube import YouTube
import colorama
from colorama import Fore
import os

# function

def Download_url(url_link):
    try:
        yt = YouTube(url_link)
        video = yt.streams.filter(only_audio=True).first()
        destination = './Download_file'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + Fore.GREEN + " has been successfully downloaded." + Fore.RESET)
    except:
        print(Fore.RED + "Error: false url -> " + Fore.RESET + url_link.replace('\n', ''))

def basic_verification():
    if os.path.exists("list/list.txt") == False:
        print(Fore.RED + "Error: file ['list/list.txt'] doesn't exist" + Fore.RESET)
        quit()

def export_file(file):
    line = file.readline()
    return (line)
    
# main

if __name__ == '__main__':

    # verif

    basic_verification()

    # try to open

    file = open("list/list.txt", "r")
    line = export_file(file)

    # Download mp3 file

    print("Download ...\n")

    while line:
        Download_url(line)
        line = export_file(file)
    print("Task finished.")