OldLines – simple plugin, helping prevent newlines at the end of the document and kill lines including ending newline.
On each document saving plugin can removes ending newlines.

# Use

To remove whole line (including ending newline) use command `kill_line`:
```
{"keys": ["ctrl+'"], "command": "kill_line"}
```

To remove blank (or whitespases) lines above cursor use command `kill_blank_lines_above`:

```
{"keys": ["shift+backspace"], "command": "kill_blank_lines_above"}
```

To remove blank (or whitespases) lines below cursor use command `kill_blank_lines_below`:

```
{"keys": ["shift+delete"], "command": "kill_blank_lines_below"}
```

To auto remove all blank (or whitespases) lines at the end of document (including ending newline) use setting `kill_ending_blank_lines_on_save`:

```
"kill_ending_blank_lines_on_save": true
```

This send command `kill_ending_blank_lines` on each file saving.


# Installation
Supports Sublime Text 2 and 3.
Use your version number in directory path.

## OS X
```
cd ~/"Library/Application Support/Sublime Text 2/Packages"
git clone https://github.com/gzzz/sublime-old-lines.git OldLines
```

## Windows
```
cd %AppData%\Sublime Text 2\Packages\
git clone https://github.com/gzzz/sublime-old-lines.git OldLines
```