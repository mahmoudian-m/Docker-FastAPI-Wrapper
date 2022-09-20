from fastapi import APIRouter
from api.docker_api.models import DockerLsResponseModel, DockerImageResponseModel, DockerNetworkResponseModel, \
    DockerImageRmResponseModel, DockerImageRmRequestModel
from api.libs import DockerWrapper
from config.config import SUCCESS_CODE

docker_wrapper = APIRouter()

ROOTPATH = '/docker/'
DOCKERTAG = 'Docker'


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


@docker_wrapper.post(ROOTPATH + 'image/rm/', response_model=DockerImageRmResponseModel, tags=[DOCKERTAG])
async def docker_service_rm(request: DockerImageRmRequestModel):
    image_rm = DockerWrapper.DockerWrapper.docker_image_rm(request.ImageID, request.Forced)
    if image_rm["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": image_rm["ResponseCode"], "Message": image_rm["Value"]}
    return {"ImageID": image_rm["Value"]}
