from fastapi import APIRouter
from api.docker_swarm_api.models import DockerNodeResponseModel, DockerServiceLsResponseModel, \
    DockerServicePsResponseModel, DockerServiceLogsResponseModel, DockerResponseModel, DockerServiceRMRequestModel,DockerServiceRMResponseModel
from api.libs import DockerWrapper
from config.config import SUCCESS_CODE

docker_swarm_wrapper = APIRouter()

ROOTPATH = '/docker_swarm/'
SWARMTAG = "DockerSwarm"


@docker_swarm_wrapper.get(ROOTPATH + 'node/ls/', response_model=DockerNodeResponseModel, tags=[SWARMTAG])
async def docker_node_ls():
    nodes = DockerWrapper.DockerWrapper.docker_node_ls()
    if nodes["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": nodes["ResponseCode"], "Message": nodes["Value"]}
    return {"Nodes": nodes["Value"]}


@docker_swarm_wrapper.get(ROOTPATH + 'service/ls/', response_model=DockerServiceLsResponseModel, tags=[SWARMTAG])
async def docker_service_ls():
    services = DockerWrapper.DockerWrapper.docker_service_ls()
    if services["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": services["ResponseCode"], "Message": services["Value"]}
    return {"Services": services["Value"]}


@docker_swarm_wrapper.get(ROOTPATH + 'service/ps/{service_name}', response_model=DockerServicePsResponseModel,
                          tags=[SWARMTAG])
async def docker_service_ps(service_name: str):
    services_ps = DockerWrapper.DockerWrapper.docker_service_ps(service_name)
    if services_ps["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": services_ps["ResponseCode"], "Message": services_ps["Value"]}
    return {"ServicesPs": services_ps["Value"]}


@docker_swarm_wrapper.get(ROOTPATH + 'service/logs/{service_name}', response_model=DockerServiceLogsResponseModel,
                          tags=[SWARMTAG])
async def docker_service_logs(service_name: str):
    services_logs = DockerWrapper.DockerWrapper.docker_service_logs(service_name)
    if services_logs["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": services_logs["ResponseCode"], "Message": services_logs["Value"]}
    return {"ServiceLogs": services_logs["Value"]}


@docker_swarm_wrapper.post(ROOTPATH + 'service/rm/', response_model=DockerServiceRMResponseModel, tags=[SWARMTAG])
async def docker_service_rm(service: DockerServiceRMRequestModel):
    service_rm = DockerWrapper.DockerWrapper.docker_service_rm(service.ServiceName)
    if service_rm["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": service_rm["ResponseCode"], "Message": service_rm["Value"]}
    return {"ServiceName": service_rm["Value"]}
