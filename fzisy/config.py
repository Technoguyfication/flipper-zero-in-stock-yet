import os

class Config:

    def __init__(self):
        self.log_level = os.environ.get("LOG_LEVEL", "INFO").upper()

        self.twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.twilio_from_number = os.environ.get("TWILIO_FROM_NUMBER")

        self._sms_broadcast_list_str = os.environ.get("SMS_BROADCAST_LIST")

        try:
            self._sms_broadcast_list = self._sms_broadcast_list_str.split(",")
        except:
            self._sms_broadcast_list = None

    def validate(self) -> tuple[bool, str | None]:
        """
        Validates the configuration and returns a tuple of a boolean and a string.
        
        The boolean indicates whether the configuration is valid or not.
        The string is the error message if the configuration is invalid."""

        if self.twilio_account_sid is None:
            return False, "TWILIO_ACCOUNT_SID is not set"

        if self.twilio_auth_token is None:
            return False, "TWILIO_AUTH_TOKEN is not set"

        if self.twilio_from_number is None:
            return False, "TWILIO_FROM_NUMBER is not set"

        if self._sms_broadcast_list is None:
            return False, "SMS_BROADCAST_LIST is not set or is not a comma separated list of phone numbers"

        return True, None
