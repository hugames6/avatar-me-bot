from stability_sdk import client
import os
import io
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import warnings
from PIL import Image
import random
import asyncio

os.chdir('stablediffusion')

async def generate_man():
    for i in range(0, 2):
        n = (random.randint(1, 100))

        with open(r"sdxl-man.txt") as file:
            prompts = file.read()
            prompts = prompts.split('\n')
            prompt = prompts[n]
            await generate_photo(prompt=prompt)

async def generate_woman():
    for i in range(0, 2):
        n = (random.randint(1, 100))

        with open(r"sdxl-woman.txt") as file:
            prompts = file.read()
            prompts = prompts.split('\n')
            prompt = prompts[n]
            await generate_photo(prompt=prompt)

async def generate_photo(prompt):
    os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
    os.environ['STABILITY_KEY'] = 'sk-yNZ4XNDHkIF6w54BNO2RSGtY2f4YCbutXUfMhqWPo4LWLKzj'

    stability_api = client.StabilityInference(key=os.environ['STABILITY_KEY'], verbose=True,engine='stable-diffusion-xl-1024-v0-9')

    answers = stability_api.generate(prompt=f'{prompt}', 
                                    steps=50, 
                                    cfg_scale=8.0, 
                                    width=256, 
                                    height=256, 
                                    samples=1, 
                                    sampler=generation.SAMPLER_K_DPMPP_2M)

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn("Неверный промпт, или ошибка его обслуживания")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save(str(artifact.seed)+ ".png")

asyncio.run(generate_woman())