#setup pydantic model|Schema Validation

from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name:str
    model_provider:str
    system_prompt:str
    messages:List[str]
    allow_search:bool

#Setup AI Agent from Frontend
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
app=FastAPI(title="Ai-Agent")

ALLOWED_MODELS=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

@app.post("/chat")
def chat_endpoit(request:RequestState):
    if request.model_name not in ALLOWED_MODELS:
         return {"error": "Not able to find the model"} 
    else:
        llm_id=request.model_name
        query = request.messages
        allow_search = request.allow_search
        system_prompt = request.system_prompt
        provider = request.model_provider

    # Create AI Agent and get response from it! 
    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return {"result": response}

#Step3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)    




    

