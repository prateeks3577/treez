echo hello
py -m pip install --upgrade pip
py -m pip install --user virtualenv
py -m venv env
CALL env\Scripts\activate
py -m pip install Flask
py -m pip install waitress
py -m pip install requests
@REM Flask --app server run
py server.py
echo %time%
echo kill for next instance
timeout 500 > NUL
echo %time%