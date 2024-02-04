import plantuml
import boto3
import os
import uuid



def generate_uuid():
    return uuid.uuid4()


def store_image(image):

    s3_client = boto3.client('s3')
    bucket_name = os.environ['BUCKET_NAME']  # The S3 bucket name passed as an environment variable
    path = os.environ['BUCKET_PATH']  # The S3 bucket name passed as an environment variable

    file_uuid = generate_uuid()
    filename = f"{path}/{file_uuid}.png"

    # Upload the image to S3
    s3_client.put_object(Body=image,
                            Bucket=bucket_name,
                            Key=filename,
                            ContentType='image/png')

    
    print(f"Filename is {filename}")
    return filename

def get_image_link(filename):

    s3_website = os.environ['S3_WEBSITE']  # The S3 bucket name passed as an environment variable
    link = f"{s3_website}{filename}"
    print(f"S3 Website {s3_website} and Filename Path {filename} and link {link}")

    return link


def create_diagram(code):
    
    print(f'plantuml code to create image {code}')
    code = plantuml.prepare_code(code)


    image = plantuml.create_plantuml_image(code)
    print(f'plantuml code to create image {image}')

    filename = store_image(image)
    print(f'filename to store the image {filename}')

    link = get_image_link(filename)
    print(f'link of the image that was stored   {link}')

    return link






# create diagram as png - return as png bytes.


