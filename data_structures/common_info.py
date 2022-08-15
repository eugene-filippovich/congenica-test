from dataclasses import dataclass


@dataclass
class Auth:
    # BASE_URL: str = "https://www.pixellu.com"
    BASE_URL: str = "https://smartslides.com"
    # APP_URL: str = "/smartslides/"
    APP_URL: str = "/login/"
    login: str = "ta_interview@pixellu.com"
    password: str = "ta_interview"
