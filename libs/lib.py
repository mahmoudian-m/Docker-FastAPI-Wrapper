import subprocess
from config.config import SUCCESS_CODE, EXCEPTION_CODE, RETURN_EXECUTION_SUCCESS_CODE


def execute_command(command):
    """

    :param command: Unix-like operating system commands
    :return: Dictionary
    """
    try:
        process = subprocess.Popen(command, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, err = process.communicate()
    except subprocess.CalledProcessError as e:
        return {'ResponseCode': EXCEPTION_CODE, 'Value': e}
    if err:
        value = err
        response_code = EXCEPTION_CODE
    elif process.returncode == RETURN_EXECUTION_SUCCESS_CODE:
        value = output.decode('utf-8').rstrip('\n')
        response_code = SUCCESS_CODE
    else:
        value = output.decode("utf-8").rstrip('\n')
        response_code = EXCEPTION_CODE
    return {'ResponseCode': response_code, 'Value': value}