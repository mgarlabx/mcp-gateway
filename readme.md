# Alternativas para desenvolver gateways de MCPs

## Introdução

Se você é novato no desenvolvimento e uso de MCPs, eu recomendo começar por esse repositório:

[MCP - O Guia Definitivo](https://github.com/mgarlabx/mcp)

## Serviços

Já existem alguns serviços prontos para servidores MCPs. Funcionam na base de assinaturas mensais. Exemplos:
- [Storm MCP](https://stormmcp.ai)
- [Traefik Labs](https://traefik.io/solutions/mcp-gateway)

São muito fáceis de serem usados, basta selecionar os servidores desejados e seu gateway já está pronto. 

O inconveniente é que só é possível usar servidores que estão disponíveis na plataforma. Se você quiser algum que ainda não foi homologado por eles, não terá como incluir no gateway, o que em alguns casos poderá ser muito limitante.

## Docker
O Docker criou um [kit](https://github.com/docker/mcp-gateway) para o desenvolvimento de MCP Gateways com muitos recursos.

É muito simples criar um gateway para uso local, em sua própria máquina, através do MCP Toolkit, veja [aqui](https://github.com/docker/mcp-gateway/blob/main/docs/mcp-gateway.md) algumas instruções.

Há várias vantagens desse uso. Por exemplo, se você usa o Claude Desktop, você não precisa fazer uma conexão para cada MCP que deseja usar. Basta criar o Docker Gateway e conectar esse gateway no Claude. Assim, toda manutenção dos conectores fica do lado do Docker e o Claude fica com apenas uma conexão.

Além disso, os MCPs rodam dentro de um container do Docker, o que protege a sua máquina ser eventuais serviços maliciosos.

Como desvantagem é a adição de servers que não estão homologados pelo próprio Docker.

Outra limitação é o deploy na nuvem de um gateway criado pelo Docker. Você precisará ter um razoável domínio de containers, bem como dos recursos disponíveis pela nuvem que irá utilizar.

## Plataformas prontas

Os provedores e serviços na nuvem estão criando suporte para MCP Gateways. Essa lista contém algumas alternativas que podem ser exploradas:

- [AWS](https://builder.aws.com/content/2xmhMS0eVnA10kZA0eES46KlyMU/how-the-mcp-gateway-centralizes-your-ai-models-tools)
- [Microsoft](https://github.com/microsoft/mcp-gateway)
- [IBM](https://github.com/IBM/mcp-context-forge)
- [Agentic Community](https://github.com/agentic-community/mcp-gateway-registry)
- [Lasso](https://github.com/lasso-security/mcp-gateway)

Ainda é tudo muito novo com relação a esse assunto, essa lista poderá ficar obsoleta rapidamente.

## Desenvolvimento em Python

É possível criar manualmente gateways de MCP. Não é um processo complexo, porém pode ser trabalhoso, pois é necessário criar uma função para cada "tool" de cada "server". É por essa razão, penso eu, que os serviços prontos que já existem (incluindo o Docker) possuem uma lista limitada de servidores MCP disponíveis.

Para aqueles que querem desenvolver o seu próprio gateway, seguem aqui algumas dicas:

### Use o Postman

O Postman está com suporte para [MCP Requests](https://learning.postman.com/docs/postman-ai-developer-tools/mcp-requests/overview/). É a ferramenta ideal para inspecionar, analisar e testar MCPs. Eu recomendo fortemente que desenvolvedores usem essa ferramenta, ao invés de usar a própria IDE (Cursor, VSCode, etc.), ou mesmo clients como Claude Desktop.

Use essas outras alternativas depois que seu gateway estiver pronto e já testado no Postman.

### Use servers remotos

Use servidores remotos para fazer os primeiros testes de seu gateway. Isso evita ter que baixar e rodar locamente servidores, o que seria uma etapa mais para debuggar. Eu sugiro esses servers:

Peek: `https://mcp.peek.com`

Remote MCP: `https://mcp.remote-mcp.com`

Hugging Face: `https://hf.co/mcp`

Esses servidores são abertos, ou seja, sem a necessidade de autenticação. Fica mais simples para quem está começando.

Se quiser uma lista mais completa de servidores remotos de MCP, aqui tem algumas opções:

- [Remote MCP](https://www.remote-mcp.com)
- [Awesome Remote MCP](https://github.com/jaw9c/awesome-remote-mcp-servers)

### Use o FastMCP
Combine o FastMCP [Server](https://gofastmcp.com/servers/server) com o FastMCP [Client](https://gofastmcp.com/clients/client) para criar o seu gateway.
Veja nesse reposiório:
- [scp_01.py](scp_01.py)
    Um exemplo simples de como criar um `server` MCP.
- [scp_02.py](scp_02.py)
    Um exemplo simples de como criar um `client` MCP.
- [scp_03.py](scp_03.py)
    Um exemplo simples de como combinar os dois.

Naturalmente, os exemplos são muito simples, não consideram servidores que requerem autenticação, tampouco contém a autenticação ao próprio gateway criado. Mas é um bom começo para quem quer desenvolver o seu próprio gateway, sem as limitações citadas anteriormente.

Obs. Existe um pacote PIP, com recursos para criar gateways, mas eu ainda não testei:
[https://pypi.org/project/mcp-gateway](https://pypi.org/project/mcp-gateway)



## Saiba mais

[The MCP Gateway: An AI Engineer's Comprehensive Guide](https://skywork.ai/skypage/en/The-MCP-Gateway:-An-AI-Engineer's-Comprehensive-Guide/1971111013272055808)

[Understanding MCP Gateway: Your Essential Guide to Seamless Connectivity](https://api7.ai/blog/understanding-mcp-gateway)




.