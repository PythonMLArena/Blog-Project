from fastapi import APIRouter,status,Response,Query,Path,Body
from pydantic import BaseModel
from typing import Optional,List,Dict
from enum import Enum
router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)
 

class Image(BaseModel):
    url :str
    alias : str

class BlogModel(BaseModel):
    title : str
    content : str
    no_comments : int
    tags : List[str] = []
    metadata: Dict[str,str] = {"key1": "value1"}
    published : Optional[bool]
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BlogModel,id: int,version: int):
    return {"data":blog, "version":version,"id":id}


# metadata example and validator min length,Elipsis for mandatory fields
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel,id: int,comment_title: int = Query(None,title="title of the comment",description="description title of the comment",alias="commentTitle"),content: str=Body('Hi How are you?',min_length=10,max_length=500,rgex="~[a-z\s]*$"),v: Optional[List[str]] = Query(["1.0","2.0","3.0"]),newone:str=Body(Ellipsis),comment_id:int=Path(None,gt=5)):
    return {"blog":blog, "comment_title":comment_title,"id":id, "content":content,"new":newone,"version":v,"comment_id":comment_id}