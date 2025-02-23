import requests
from fastapi import APIRouter
from backend_server.model.veris_core import ChatRequestModel, ChatResponseModel
from backend_server.utils.settings import settings
from backend_server.utils.veris_core import get_payload
from backend_server.utils.text_formatter import format_response

core_router = APIRouter(prefix="/api/core")

headers = {"Authorization": "Bearer {}".format(settings.apikey)}


@core_router.post("/chat", status_code=200, name="chat_veris", response_model=ChatResponseModel)
def chat_veris(request: ChatRequestModel):

    payload = get_payload(request.message,)
    response = requests.post(settings.api_url, headers=headers, json=payload)
    return ChatResponseModel(
        veris_response=format_response(response.json()[0].get("generated_text"))
    )


