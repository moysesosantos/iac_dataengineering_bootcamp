Criando um stream de dados com Kinesis

Aqui vamos criar um Stream de Dados, vamos fazer o deploy de:

    Kinesis Stream
    Kinesis Delivery Stream
    Kinesis Firehose
    Log Group
    Log Stream
    Bucket
    IAM Role
    IAM Policy

Deploy:

    Navegue até a página do Cloudformation no seu console AWS
    Clique em create stack -> with new resources
    Faça o upload do arquivo YAML e siga as instruções para fazer o deploy

Uso:

    Recomendável criar um virtual-env

    pip install virtualenv
    cd my-project/
    virtualenv venv
    source venv/bin/activate
    # venv\Scripts\activate.bat no Windows

    Instalar as dependências de requirements.txt

    pip install -r requirements.txt

    Adicione as suas credenciais da AWS à variáveis de ambiente
        Crie um profile em ~/.aws/config

        [profile my_aws_profile]
        aws_access_key_id = AK... 
        aws_secret_access_key = sl...
        region = us-east-1

        Adicione ao ambiente: export AWS_PROFILE=my_aws_profile ou adicione ao seu .bashrc se quiser persistir a variável para outras sessões
        Execute o script Python put_records_in_kinesis.py

Seu stream de eventos agora é enviado para o Kinesis, e de lá persistido no S3.