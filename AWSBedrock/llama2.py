import boto3 
import json

prompt_data="""
Act as a Shakespeare and write a poem on India's Invinciblity in Test cricket at home
"""

bedrock = boto3.client(service_name ="bedrock-runtime")

payload ={
    "prompt": "[INST]"+ prompt_data + "[/INST]",
    "max_gen_len":512,
    "temperature": 0.5,
    "top_p":0.9
}

model_id ="meta.llama2-70b-chat-v1"
body = json.dumps(payload)
response = bedrock.invoke_model(
    body= body,
    modelId = model_id,
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())
response_text = response_body['generation']
print(response_text)