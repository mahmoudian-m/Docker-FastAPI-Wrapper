from fastapi import APIRouter
from api.docker_api.models import DockerLsResponseModel, DockerImageResponseModel, DockerNetworkResponseModel
from api.libs import DockerWrapper
from config.config import SUCCESS_CODE

docker_wrapper = APIRouter()

ROOTPATH = '/docker/'
DOCKERTAG = 'Docker'
SWARMTAG = "Docker Swarm"


@docker_wrapper.get(ROOTPATH + 'container/ls/', response_model=DockerLsResponseModel, tags=[DOCKERTAG])
async def docker_container_ls():
    containers = DockerWrapper.DockerWrapper.docker_container_ls()
    if containers["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": containers["ResponseCode"], "Message": containers["Value"]}
    return {"Containers": containers["Value"]}


@docker_wrapper.get(ROOTPATH + 'image/ls/', response_model=DockerImageResponseModel, tags=[DOCKERTAG])
async def docker_image_ls():
    images = DockerWrapper.DockerWrapper.docker_image_ls()
    if images["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": images["ResponseCode"], "Message": images["Value"]}
    return {"Images": images["Value"]}


@docker_wrapper.get(ROOTPATH + 'network/ls/', response_model=DockerNetworkResponseModel, tags=[DOCKERTAG])
async def docker_network_ls():
    networks = DockerWrapper.DockerWrapper.docker_network_ls()
    if networks["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": networks["ResponseCode"], "Message": networks["Value"]}
    return {"Networks": networks["Value"]}

