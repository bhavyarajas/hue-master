import json
from backend.models.vae import VAEModel

vae = VAEModel()

def handler(request, context):
    grid = vae.generate_grid(level="medium", shape=(5, 6))
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": json.dumps({"grid": grid.tolist()})
    }