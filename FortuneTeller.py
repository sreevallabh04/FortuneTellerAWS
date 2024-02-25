import json
import random

def lambda_handler(event, context):
    fortunes = [
        "You will have a great day!",
        "Something unexpected will happen soon.",
        "You will meet someone important.",
        "A surprise is waiting for you.",
        "Your hard work will pay off soon."
    ]

    selected_fortune = random.choice(fortunes)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': selected_fortune
        })
    }
