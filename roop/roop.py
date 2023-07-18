import replicate
import os

def roop_deepfake():
    output = replicate.Client(api_token='r8_T2MmSOk9UHnQTsrFJmwWylsqUe0lPIA0zMI88')
    image = output.run(
        "okaris/roop:68983710077a769e47038f519fd3620e6d7023f4ac02c8c85612d71a32f696d6",
        input = {f"target": open(f'template.png', "rb"),
                'source': open(f'user.jpg', "rb")}
    )
    for i in image:
        print(i)
        return i