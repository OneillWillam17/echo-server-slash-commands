import subprocess
import requests


class Echo:
    def __init__(self):
        # api url is used to get the session id so we can make a spark link for players to join from
        self.api_url = "http://127.0.0.1:6721/session"
        self.path = r"C:\Program Files\Oculus\Software\Software\ready-at-dawn-echo-arena\bin\win10\echovr.exe"
        # dict is used to translate common names for the server locations to the accepted params when launching the game
        self.server_dict = {
            "chicago": 'uscn',  # uscn - United States Central North etc...
            "texas": 'usc',
            'us_east': 'use',
            'us_west': 'usw',
        }

    def open_temp_server(self, location: str):
        """Opens EchoVr.exe with the location of the server passed in the args when method is called"""
        try:
            subprocess.Popen([self.path, '-region', location, '-spectatorstream'])
        except FileNotFoundError as file:
            error_message = f"echovr.exe path is incorrect: {self.path}\nTry setting new echovr path using .path"
            raise FileNotFoundError(error_message) from file

    def create_spark_link(self) -> str:
        """Gets the session id from the local api then converts it into a clickable spark link"""
        json = requests.get(self.api_url).json()
        session_id = json['sessionid'].upper()
        return f"<spark://c/{session_id}>"

