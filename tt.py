#!/usr/local/Caskroom/miniforge/base/bin/python3
files=*.csv
echo "Data sets:", $files
echo
echo "Run IO test"
echo
python3 test_io.py $files
echo
echo "Run Tests"
echo
python3 test_stats.py $files