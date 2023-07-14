import 

os.chdir('stablediffusion')
with open(r"man.txt") as file:
    prompts = file.read()
    print(prompts)