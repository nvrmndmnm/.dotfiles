#!/bin/bash

# ExecStart=gpu-screen-recorder -v no -w "${WINDOW}" -s "${OUTPUT_RESOLUTION}" -c "${CONTAINER}" -q "${QUALITY}" -k "${CODEC}" -ac "${AUDIO_CODEC}" -a "${AUDIO_DEVICE}" -a "${SECONDARY_AUDIO_DEVICE}" -f "${FRAMERATE}" -r "${REPLAYDURATION}" -o "${OUTPUTDIR}" -df "${MAKEFOLDERS}" $ADDITIONAL_ARGS -cr "${COLOR_RANGE}" -keyint "${KEYINT}" -restore-portal-session "${RESTORE_PORTAL_SESSION}" -encoder "${ENCODER}" -bm "${BITRATE_MODE}"

gpu-screen-recorder \
    -w focused \
    -s 3840x2160 \
    -f 60 \
    -c mp4 \
    -a "default_output|default_input" \
    -r 300 \
    -o "$HOME/videos"