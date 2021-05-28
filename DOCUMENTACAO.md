# Documentação da API

Nesse arquivo voce encontra a documentação para todas as rotas criadas ate agora na aplicação.
## Rotas

- Produção: `https://podclass.herokuapp.com`
- Local: `http://your_ip:5000`

### /podcast

#### GET
@Returns a list of podcasts
```json
{
    "id": "uuidv4",
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
Insert a new feed rss
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
Get all episodes available

@Returns a list of episodes
```json
{
    "id": "string",
    "title": "string",
    "members": "string",
    "published": "string",
    "thumbnail": "string",
    "description": "string",
    "file": "object",
    "podcast_id": "string"
}