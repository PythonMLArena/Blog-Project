from fastapi import APIRouter,status,Response
from typing import Optional
from enum import Enum
router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

# QueryParameters Example (any function parameter which are not part of the path)

@router.get("/all/")
def get_all_blogs(page_number:int =1,page_size:int =10):
    return {"message":f"Hello we are on page number = {page_number} with Pagesize = {page_size}!"}


# @router.get('/blog/{id}',tags=["Path Parameter"])
# def get_blog(id):
#     return {"message":f"Hello we got the blog with id = {id}!"}


# Path Parameter with type validation Example
# Uses Pydantic to validate the types of parameters, provide the data conversion accordingly
# Order is important according to the url we define here
@router.get('/{id}')
def get_blog(id: int):
    return {"message":f"Hello we got the blog with id = {id}!"}


# Predefined Values Example
class BlogType(str,Enum):
    short='short'
    story='story'
    howto='howto'


@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message":f"Hello we got the all blog with type = {type}!"}


@router.get("/{id}",status_code=status.HTTP_200_OK,summary="Understand the Status code here",response_description="The Understand the status code in the response")
def get_blog_by_id(id:int ,response: Response):
    """
        - **id**: The id of for to retrive the blog id,
        - **response**: Response is for customization
    """
    if id>1:
        response.status_code=status.HTTP_200_OK
        return {"message":f"Hello we are on blog number = {id} !"}
    else:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"message":f"wrong request !"}
    

@router.get("/{id}/comments/{commentid}",tags=["comment"])
def get_blog_comments(id:int =1,commentid:int =1,valid:bool = True, page_size:int =10):
    if valid:
        return {"message":f"Hello we are on blog number = {id} and commentid {commentid} with Pagesize = {page_size}!"}
    else:
        return {"message":f"wrong request !"}
    