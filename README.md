# Testing AWS Lambda Locally with SAM 

[![aws](https://cdn3.emoji.gg/emojis/8708-aws.png)](https://emoji.gg/emoji/8708-aws)

This guide provides detailed steps on how to set up and test an AWS Lambda function locally using the AWS Serverless Application Model (SAM).



1. **Initialize a SAM Project:**

   Start by initializing a new SAM project. Run the following command and follow the prompts, including entering a project name (e.g., `sam-demo`).

   ```bash
   sam init

2. **Edit the template.yaml File:**

    Open the template.yaml file in your project directory. Modify it to define your Lambda function, including necessary configurations and resources.


3. **Modify the event.json file.** 

    This file should reflect the event data that your Lambda function will consume. Ensure the structure matches what your Lambda function expects.

    ```bash
    {
    "key1": "value1",
    "key2": "value2"
    }
    ```

4. **Set Up Dependencies:**

    Specify all the necessary dependencies in the requirements.txt file. This file should list all Python packages required by your Lambda function.

5. **Build the Project:**

    Build your SAM project to prepare it for local testing. This will compile your function and its dependencies into a .aws-sam directory.

    ```bash
    sam build
    ```

6. **Invoke the Lambda Function Locally:**

    Finally, invoke your Lambda function locally to test it. Use the following command, replacing ChatFunction with your function's name and specifying the path to your event.json file.

    ```bash
    sam local invoke ChatFunction -e events/event.json
    ```

This command will simulate the Lambda execution environment on your local machine and process the event defined in event.json.