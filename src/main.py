import os

# Read env variable
env_var = os.environ.get('INPUT_WHO-TO-GREET')
print('Hello ' + env_var)