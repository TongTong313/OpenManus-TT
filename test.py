from pydantic import BaseModel, Field
from typing import List, Optional
import datetime


class Article(BaseModel):
    id: int
    title: str
    content: str
    tags: List[str] = []
    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime] = None

    class Config:
        # 允许从ORM对象创建
        from_attributes = True
        # 使用别名
        populate_by_name = True
        # JSON序列化时将日期转为ISO格式
        json_encoders = {datetime.datetime: lambda v: v.isoformat()}
        # # 验证示例
        # json_schema_extra = {
        #     "example": {
        #         "id": 1,
        #         "title": "Pydantic教程",
        #         "content": "这是一篇关于Pydantic的教程",
        #         "tags": ["python", "pydantic"],
        #         "created_at": "2023-01-01T00:00:00"
        #     }
        # }


a = Article(id=1,
            title="Pydantic教程",
            content="这是一篇关于Pydantic的教程",
            tags=["python", "pydantic"],
            created_at=datetime.datetime.now())

article = a.model_dump_json()
print(article)
