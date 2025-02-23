from pydantic import BaseModel


class ChatRequestModel(BaseModel):
    message: str
    user_id: str = None


class ChatResponseModel(BaseModel):
    veris_response: str