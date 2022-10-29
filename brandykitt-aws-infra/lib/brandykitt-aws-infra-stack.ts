import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apiGateway from 'aws-cdk-lib/aws-apigateway';
import * as dotenv from 'dotenv';
import { Duration } from 'aws-cdk-lib';

dotenv.config();

export class BrandykittAwsInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const layer = new lambda.LayerVersion(this, 'BaseLayer', {
      code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_7],
    })

    const apiLambda = new lambda.Function(this, 'BrandykittLambdaFunction', {
      runtime: lambda.Runtime.PYTHON_3_7,
      code: lambda.Code.fromAsset("../app/"),
      handler: "brandykitt_api.handler",
      layers: [layer],
      environment: {
        "OPENAI_API_KEY": process.env.OPENAI_API_KEY!,
      },
      timeout: Duration.seconds(30),
    });
    
    // create the actual api
    const brandykittApi = new apiGateway.RestApi(this, 'BrandyKittApi',{
      restApiName: "BrandyKitt Api"
    })

    // integrate lambda and and add proxy so api gateway doesn't fully process the incoming request and just pass onto the lambda function to handle
    brandykittApi.root.addProxy({
      defaultIntegration: new apiGateway.LambdaIntegration(apiLambda)
    })
  }
}