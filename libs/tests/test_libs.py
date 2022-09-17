from libs.lib import execute_command
from config.config import SUCCESS_CODE


def test_execute_command_return_code():
    assert execute_command("ls")["ResponseCode"] == SUCCESS_CODE

