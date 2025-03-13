from pydantic import BaseModel, Field


class LLM:

    def __init__(self, model: str = "gpt-3.5-turbo", temperature: float = 0.5):
        self.model = model
        self.temperature = temperature


class User(BaseModel):
    name: str = Field(..., description="The name of the user")
    age: int = Field(..., description="The age of the user")
    # default_factory会创建一个LLM实例
    llm: LLM = Field(default_factory=LLM, description="The LLM model to use")

    class Config:
        arbitrary_types_allowed = True


if __name__ == "__main__":
    user = User(name="John", age=20)
    print(user)
