Deploy DMS

O deploy do DMS vai falhar se a sua conta na AWS não tiver um dms-vpc-role definido. Mais informações veja a documentação do cloudformation.

Para criar o role podemos ir no painel do iam, criar um role, selecionando o DMS como serviço. E adicionar a seguinte política: AmazonDMSVPCManagementRole.

Mais informações: https://forums.aws.amazon.com/thread.jspa?messageID=921775