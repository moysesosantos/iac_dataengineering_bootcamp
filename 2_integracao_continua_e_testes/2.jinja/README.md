Utilizando GitHub Actions

Como usar:

    Defina as suas credenciais da AWS dentro do seu repositório no GitHub.
        Acesse o repositório e vá em settings -> secrets
        Adicione as credenciais de um usuário que tenha permissões suficientes para fazer deploy de templates Cloudformation
            AWS_ACCESS_KEY_ID
            AWS_DEFAULT_REGION
            AWS_SECRET_ACCESS_KEY
        Adicione as variáveis de ambiente necessárias
            redshiftClusterMasterUsername
            redshiftClusterMasterUserPassword

Deploy para staging

    Crie um branch chamado 2.jinja_staging
        git checkout -b 2.jinja_staging
    O arquivo que vai controlar este workflow está em .github/workflows/2.jinja_staging.yml
        Crie um comit e faça push para o seu repositório remoto
        O workflow será executado ao fazer push para o branch 2.jinja_staging
    Veja o GitHub fazer deploy da sua infraestrutura dentro da aba Actions

Deploy para production

    Crie um branch chamado 2.jinja_production
        git checkout -b 2.jinja_production
    O arquivo que vai controlar este workflow está em .github/workflows/2.jinja_production.yml
        Crie um comit e faça push para o seu repositório remoto
        O workflow será executado ao fazer push para o branch 2.jinja_production
    Veja o GitHub fazer deploy da sua infraestrutura dentro da aba Actions

Lembre de sembre deletar os seus stacks depois da aula para evitar custos inesperados na sua fatura da AWS!