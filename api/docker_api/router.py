from fastapi import APIRouter
from api.docker_api.models import DockerLsResponseModel
from libs import DockerWrapper
from config.config import SUCCESS_CODE, EXCEPTION_CODE

docker_wrapper = APIRouter()

ROOTPATH = '/docker/'
TAG = 'Docker'


@docker_wrapper.get(ROOTPATH + 'ls/', response_model=DockerLsResponseModel, tags=[TAG])
async def docker_container_ls():
    containers = DockerWrapper.docker_container_ls()
    print(containers)
    if containers["ResponseCode"] != SUCCESS_CODE:
        return {"ErrorCode": containers["ResponseCode"], "Message": containers["Value"]}
    result = {"Containers": containers["Value"]}
    return result
