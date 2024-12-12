import subprocess
import sys
import re

def get_default_sink():
    result = subprocess.run(["pactl", "get-default-sink"], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

def list_sinks_short():
    result = subprocess.run(["pactl", "list", "short", "sinks"], stdout=subprocess.PIPE, text=True)
    sinks = []
    for line in result.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            sink_id, sink_name = parts[0], parts[1]
            sinks.append((sink_id, sink_name))
    return sinks

def list_sinks():
    result = subprocess.run(["pactl", "list", "sinks"], stdout=subprocess.PIPE, text=True)
    sinks = []
    sink_id, sink_name, description = None, None, None

    for line in result.stdout.splitlines():
        id_match = re.match(r"^Sink #(\d+)", line)
        if id_match:
            if sink_id and sink_name and description:
                sinks.append((sink_id, sink_name, description))
            sink_id, sink_name, description = id_match.group(1), None, None
            continue
        
        name_match = re.match(r"^\s+Name: (.+)", line)
        if name_match:
            sink_name = name_match.group(1)
            continue
        
        desc_match = re.match(r"^\s+Description: (.+)", line)
        if desc_match:
            description = desc_match.group(1)

    if sink_id and sink_name and description:
        sinks.append((sink_id, sink_name, description))

    return sinks

def set_default_sink(sink_name):
    subprocess.run(["pactl", "set-default-sink", sink_name])

def run_rofi(title, options):
    rofi_command = ["rofi", "-dmenu", "-i", "-p", title, "-theme", "~/.config/rofi/launchers/style.rasi"]
    input_text = "\n".join(options)
    result = subprocess.run(rofi_command, input=input_text, text=True, stdout=subprocess.PIPE)
    return result.stdout.strip()

def main():
    sinks = list_sinks()
    default_sink = get_default_sink()
    
    sink_options = [
        f"{'* ' if sink_name == default_sink else '  '}{description}" for _, sink_name, description in sinks
    ]
    sink_selection = run_rofi("Select Audio Output", sink_options)
    
    if sink_selection:
        selected_description = sink_selection.strip('* ')
        selected_sink = next((sink_name for _, sink_name, description in sinks if description == selected_description), None)
        
        if selected_sink:
            set_default_sink(selected_sink)
    else:
        sys.exit()    

if __name__ == "__main__":
    main()
