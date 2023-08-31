import torch
from transformers import pipeline
from fastapi import FastAPI
import uvicorn
import os

model_name = "databricks/dolly-v2-3b"

current_path = os.path.dirname(os.path.abspath(__file__))
generate_text = pipeline(model=model_name,
                         torch_dtype=torch.bfloat16,
                         trust_remote_code=True,
                         device_map="auto")

app = FastAPI()


@app.post("/chat_api")
async def chat(text: dict):
    res = generate_text(text)
    generated_text = res[0]["generated_text"]
    reply = generated_text.replace('\n', '<br>')
    print(f'input:{text} reply:{reply}')

    outJson = {
        "output": [
            {
                "type": "text",
                "value": reply
            }
        ]
    }
    return outJson



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)