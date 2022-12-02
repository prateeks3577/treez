echo hello
py -m pip install --upgrade pip
py -m pip install --user virtualenv
py -m venv env
CALL env\Scripts\activate
py -m pip install Flask
py -m pip install waitress
py -m pip install requests
py client.py
@REM py server.py
echo %time%
timeout 5 > NUL
echo %time%