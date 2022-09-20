import json
import re
import subprocess
from config.config import SUCCESS_CODE, EXCEPTION_CODE, RETURN_EXECUTION_SUCCESS_CODE


class DockerWrapper:
    docker_ls = """docker container ls --all --format '{"ContainerID":"{{ .ID }}", "Image": "{{ .Image }}", "CreatedAt":"{{ .CreatedAt }}","Status":"{{.Status}}","Ports":"{{.Ports}}","ContainerName":"{{.Names}}","Mounts":"{{.Mounts}}","RunningFor":"{{.RunningFor}}"}'
        """
    image_ls = """docker image ls --format '{"ContainerID":"{{ .ID }}","CreatedAt":"{{.CreatedAt}}","CreatedSince":"{{.CreatedSince}}","ID":"{{.ID}}","Repository":"{{.Repository}}","Size":"{{.Size}}","Tag":"{{.Tag}}"}'"""
    network_ls = """docker network ls --format '{"ID":"{{ .ID }}","Name":"{{.Name}}","Driver":"{{.Driver}}","Scope":"{{.Scope}}"}'"""
    node_ls = """docker node ls --format '{"Availability":"{{ .Availability }}","EngineVersion":"{{.EngineVersion}}","Hostname":"{{.Hostname}}","ID":"{{.ID}}","ManagerStatus":"{{.ManagerStatus}}","Status":"{{.Status}}"}'"""
    service_ls = """docker service ls  --format '{"ID":"{{ .ID }}","Name":"{{.Name}}","Image":"{{.Image}}","Mode":"{{.Mode}}","Ports":"{{.Ports}}","Replicas":"{{.Replicas}}"}'"""
    service_ps = """ "{'CurrentState':'{{.CurrentState}}','DesiredState':'{{.DesiredState}}','Error':'{{.Error}}','ID':'{{.ID}}','Image':'{{.Image}}','Name':'{{.Name}}','Node':'{{.Node}}','Ports':'{{.Ports}}'}" """
    service_logs = "docker service logs --no-trunc --raw {}"
    service_rm = "docker service rm {}"

    @staticmethod
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

    @staticmethod
    def parsing_docker_output(output):
        """
        :param output: docker command result
        :return: docker json result
        """
        value = []
        for items in output.split('\n'):
            value.append(json.loads(items))
        return value

    @staticmethod
    def docker_container_ls():
        result = DockerWrapper.execute_command(DockerWrapper.docker_ls)
        if result['ResponseCode'] == SUCCESS_CODE:
            parsed_result = DockerWrapper.parsing_docker_output(result["Value"])
            return {'ResponseCode': SUCCESS_CODE, 'Value': parsed_result}
        else:
            return {'ResponseCode': result['ResponseCode'], 'Value': result['Value']}

    @staticmethod
    def docker_image_ls():
        result = DockerWrapper.execute_command(DockerWrapper.image_ls)
        if result['ResponseCode'] == SUCCESS_CODE:
            parsed_result = DockerWrapper.parsing_docker_output(result["Value"])
            return {'ResponseCode': SUCCESS_CODE, 'Value': parsed_result}
        else:
            return {'ResponseCode': result['ResponseCode'], 'Value': result['Value']}

    @staticmethod
    def docker_network_ls():
        result = DockerWrapper.execute_command(DockerWrapper.network_ls)
        if result['ResponseCode'] == SUCCESS_CODE:
            parsed_result = DockerWrapper.parsing_docker_output(result["Value"])
            return {'ResponseCode': SUCCESS_CODE, 'Value': parsed_result}
        else:
            return {'ResponseCode': result['ResponseCode'], 'Value': result['Value']}

    @staticmethod
    def docker_node_ls():
        result = DockerWrapper.execute_command(DockerWrapper.node_ls)
        if result['ResponseCode'] == SUCCESS_CODE:
            parsed_result = DockerWrapper.parsing_docker_output(result["Value"])
            return {'ResponseCode': SUCCESS_CODE, 'Value': parsed_result}
        else:
            return {'ResponseCode': result['ResponseCode'], 'Value': result['Value']}

    @staticmethod
    def docker_service_ls():
        result = DockerWrapper.execute_command(DockerWrapper.service_ls)
        if result['ResponseCode'] == SUCCESS_CODE:
            if not result["Value"]:
                return {'ResponseCode': EXCEPTION_CODE, 'Value': "Nothing found in stack"}
            parsed_result = DockerWrapper.parsing_docker_output(result["Value"])
            return {'ResponseCode': SUCCESS_CODE, 'Value': parsed_result}
        else:
            return {'ResponseCode': result['ResponseCode'], 'Value': result['Value']}

    @staticmethod
    def docker_service_ps(service_name):
        result = DockerWrapper.execute_command(f"docker service ps {service_name} --format " + DockerWrapper.service_ps)
        if result['ResponseCode'] == SUCCESS_CODE:
            parsed_result = DockerWrapper.parsing_docker_output(result["Value"].replace('"', "").replace("\'", "\""))
            return {'ResponseCode': SUCCESS_CODE, 'Value': parsed_result}
        else:
            return {'ResponseCode': result['ResponseCode'], 'Value': result['Value']}

    @staticmethod
    def docker_service_logs(service_name):
        result = DockerWrapper.execute_command(DockerWrapper.service_logs.format(service_name))
        if result['ResponseCode'] == SUCCESS_CODE:
            return {'ResponseCode': SUCCESS_CODE, 'Value': result['Value'].replace("\n", "")}
        else:
            return {'ResponseCode': result['ResponseCode'], 'Value': result['Value']}

    @staticmethod
    def docker_service_rm(service_name):
        result = DockerWrapper.execute_command(DockerWrapper.service_rm.format(service_name))
        if result['ResponseCode'] == SUCCESS_CODE:
            return {'ResponseCode': SUCCESS_CODE, 'Value': result['Value']}
        else:
            return {'ResponseCode': result['ResponseCode'], 'Value': result['Value']}