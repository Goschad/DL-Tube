## DL-Tube

#### Download several YouTube videos in mp3 via the list.txt file

### Dependency :

- `pytube`
- `colorama`

### Setup dependency :

- `./dependence/windows.sh` for Windows
- `./dependence/macos.sh` for macOs

### How to use it :

In `list/list.txt` put youtube url separated by newline like this :

```txt
https://www.youtube.com/watch?v=exemple_1
https://www.youtube.com/watch?v=exemple_2
https://www.youtube.com/watch?v=exemple_3
https://www.youtube.com/watch?v=exemple_4
```

### Run :

```bash
python main.py
```

a folder named `Download_file` will be created, with the mp3 files inside.
