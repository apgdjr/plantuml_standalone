# PlantUML Diagram Generator

## Overview

This project provides a serverless application to generate PlantUML diagrams from code snippets, store the generated diagrams in an AWS S3 bucket, and return accessible URLs to the stored images. It leverages AWS Lambda for processing and S3 for storage, making it highly scalable and cost-effective for users who need to generate UML diagrams programmatically.

## Features

- **PlantUML Diagram Generation**: Converts PlantUML code snippets into images.
- **AWS S3 Storage**: Stores generated diagrams in a specified S3 bucket.
- **Serverless Architecture**: Utilizes AWS Lambda for processing, ensuring scalability and cost efficiency.
- **Accessible URLs**: Returns URLs for each stored diagram, allowing easy access and sharing.

## Use Case

### Generating a UML Diagram for Documentation

Developers often need to include UML diagrams in their documentation to explain the architecture or workflow of their application. Using this application, a developer can write PlantUML code for the desired diagram and use the provided Lambda function to generate and store the diagram. The returned URL can then be embedded in their documentation, providing a visual representation of the architecture or workflow.

**Example**: A developer wants to create a sequence diagram to represent the authentication flow in their application. They write the PlantUML code for the sequence diagram and send it to the Lambda function. The function generates the diagram, stores it in S3, and returns a URL that the developer can include in the application's documentation.

## Getting Started

### Prerequisites

- AWS account
- AWS CLI configured
- SAM CLI

### Deployment

1. Clone this repository to your local machine.
2. Navigate to the project directory and use SAM CLI to build the application: `sam build`.
3. Deploy the application to your AWS account: `sam deploy --guided`.
4. Follow the prompts to specify your deployment parameters, including the S3 bucket name, path, and website configuration.

### Usage

1. Invoke the Lambda function with a JSON payload containing your PlantUML code snippet in the `data` field.
2. The function will process the PlantUML code, generate an image, store it in the specified S3 bucket, and return a URL to access the image.
3. Use the returned URL to access or embed your generated PlantUML diagram.

## Configuration

- `BUCKET_NAME`: Name of the S3 bucket to store the generated diagrams.
- `BUCKET_PATH`: Path within the S3 bucket to store the diagrams.
- `S3_WEBSITE`: Base URL of the S3 bucket configured for static website hosting.

## Resources

- `template.yaml`: Contains the AWS SAM template that defines the AWS resources used by this application.
- `use_case.py`: Contains the logic for generating PlantUML diagrams and storing them in S3.
- `app.py`: The handler function for the AWS Lambda, serving as the entry point for the application.
- Additional utility scripts for processing PlantUML code and managing diagrams.

