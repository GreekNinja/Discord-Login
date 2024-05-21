@echo off
title Discord Login Script

rem Install required packages
pip install -r requirements.txt

rem Run the Python script
echo Running Discord login script...
python discord_login.py
echo.
:menu
echo Choose an option:
echo 1. Restart
echo 2. Close
choice /c 12 /n
if errorlevel 2 goto close
if errorlevel 1 goto restart

:restart
echo Restarting Discord login script...
python discord_login.py
echo.
goto menu

:close
echo Closing...
