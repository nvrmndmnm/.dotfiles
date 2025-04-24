#!/usr/bin/python

import sys
import json
import subprocess

def get_keyboard_state():
    try:
        layout = subprocess.check_output(
            ["xkblayout-state", "print", "%s"],
            text=True
        ).strip().lower()

        caps = subprocess.check_output(
            ["xset", "-q"], text=True
        ).lower().count("caps lock:   on") > 0

        return layout, caps
    except Exception as e:
        return "us", False

def get_layout_symbol(layout, caps):
    symbols = {
        "ru": {
            True: "🔴",
            False: "🟠"
        },
        "us": {
            True: "🔴",
            False: ""
        }
    }
    
    return symbols.get(layout, {}).get(caps, "⚪")

def print_line(message):
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line():
    try:
        line = sys.stdin.readline().strip()
        if not line:
            sys.exit(3)
        return line
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    # Skip version header
    print_line(read_line())
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)
        
        layout, caps = get_keyboard_state()
        symbol = get_layout_symbol(layout, caps)
        
        j.insert(0, {
            'full_text': f'{symbol}',
            'name': 'keyboard',
            'color': '#FF0000' if caps else '#FFFFFF'
        })
        
        print_line(prefix + json.dumps(j))
