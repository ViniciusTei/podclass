# Documentação da API

Nesse arquivo voce encontra a documentação para todas as rotas criadas ate agora na aplicação.
## Rotas

- Produção: `https://podclass.herokuapp.com`
- Local: `http://your_ip:5000`

### /podcast

#### GET
Retorna uma lista de todos os podcasts no banco.

@Returns a list of podcasts
```json
{
    "id": "string",
    "title": "string",
    "link": "string",
    "authors": "string",
    "language": "string",
    "summary": "string",
    "tags": "array",
    "image_url": "string",
    "total_episodes": "integer"
}
```
#### POST
Adiciona um novo feed ao banco.

@Receive a body with a rss url
```json
{
    "url": "http://example.com/rss"
}
```
@Returns the podcasts inserted
```json
{
    "id": "string",
    "title": "string",
    "link": "string",
    "authors": "string",
    "language": "string",
    "summary": "string",
    "tags": "array",
    "image_url": "string",
    "total_episodes": "integer"
}
```

### /episodes

#### GET
Retorna uma lista de todos os episódios disponíveis.

Você pode chamar essa forma passando os parametros de paginação `limit` e `offset`. <br >
Da forma: `/episodes?limit=10&offset=2` <br >
Se não for passado os parametros o padrão é `?limit=20&offset=1`

@Returns a list of episodes
```json
{
    "id": "string", 
    "title": "string",
    "members": "string",
    "published": "string",
    "thumbnail": "string",
    "description": "string",
    "file": "string",
    "podcast_id": "string"
}