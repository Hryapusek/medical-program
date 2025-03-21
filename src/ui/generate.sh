#!/usr/bin/bash

for f in *.ui
do
  pyuic5 "${f}" -o "ui_${f%.ui}.py"
done
