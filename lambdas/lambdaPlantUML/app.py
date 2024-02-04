import json
import use_case

# handler - receive request payload (plantuml code) and return a s3 link to the file created in our planuml server

def get_plantuml(event):

    # Parse the stringified event body to a Python dictionary
    body = json.loads(event.get('body', '{}'))

    # Retrieve the 'data' parameter from the body
    client_data = body.get('data')

   

    return client_data


def lambda_handler(event, context):


   
    plantuml_code = get_plantuml(event)

    link_diagram = use_case.create_diagram(plantuml_code)

    return_message = {
        "status": 200,
        "url" : link_diagram
    }

    return return_message

if __name__ == "__main__":
    pass
