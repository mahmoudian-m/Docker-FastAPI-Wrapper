from libs.lib import execute_command
import json
from config.config import SUCCESS_CODE, EXCEPTION_CODE


def docker_container_ls():
    command = """
    docker container ls --all --format '{"ContainerID":"{{ .ID }}", "Image": "{{ .Image }}", "CreatedAt":"{{ .CreatedAt }}","Status":"{{.Status}}","Ports":"{{.Ports}}","ContainerName":"{{.Names}}","Mounts":"{{.Mounts}}","RunningFor":"{{.RunningFor}}"}'
    """
    result = execute_command(command)
    if result['ResponseCode'] == SUCCESS_CODE:
        value = []
        for container in result['Value'].split('\n'):
            value.append(json.loads(container))
        return {'ResponseCode': SUCCESS_CODE, 'Value': value}
    else:
        return {'ResponseCode': result['ResponseCode'], 'Value': result['Value']}

