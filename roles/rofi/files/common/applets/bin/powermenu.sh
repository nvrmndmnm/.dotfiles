theme="$HOME/.config/rofi/applets/style.rasi"

list_col='1'
list_row='6'

# Options
layout=`cat ${theme} | grep 'USE_ICON' | cut -d'=' -f2`
if [[ "$layout" == 'NO' ]]; then
	option_1=" Lock"
	option_2=" Logout"
	option_3=" Suspend"
	option_4=" Hibernate"
	option_5=" Reboot"
	option_6=" Shutdown"
	yes=' Yes'
	no=' No'
else
	option_1=""
	option_2=""
	option_3=""
	option_4=""
	option_5=""
	option_6=""
	yes=''
	no=''
fi

# Rofi CMD
rofi_cmd() {
	rofi -theme-str "listview {columns: $list_col; lines: $list_row;}" \
		-dmenu \
		-theme ${theme}
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$option_1\n$option_2\n$option_3\n$option_4\n$option_5\n$option_6" | rofi_cmd
}

# Execute Command
run_cmd() {
	if [[ "$1" == '--opt1' ]]; then
		betterlockscreen -l
	elif [[ "$1" == '--opt2' ]]; then
		'kill -9 -1'
	elif [[ "$1" == '--opt3' ]]; then
		'mpc -q pause' 'amixer set Master mute' 'systemctl suspend'
	elif [[ "$1" == '--opt4' ]]; then
		'systemctl hibernate'
	elif [[ "$1" == '--opt5' ]]; then
		'systemctl reboot'
	elif [[ "$1" == '--opt6' ]]; then
		'systemctl poweroff'
	fi
}

# Actions
chosen="$(run_rofi)"
case ${chosen} in
    $option_1)
		run_cmd --opt1
        ;;
    $option_2)
		run_cmd --opt2
        ;;
    $option_3)
		run_cmd --opt3
        ;;
    $option_4)
		run_cmd --opt4
        ;;
    $option_5)
		run_cmd --opt5
        ;;
    $option_6)
		run_cmd --opt6
        ;;
esac

