# Graphene Luna Starter Project

Starter template for using Graphane Luna with Django.

See [Graphene Luna](https://github.com/cognitive-space/graphene-luna) for more usage information.

## Setup

```bash
git clone git@github.com:cognitive-space/graphene-luna-starter.git
cd graphene-luna-starter
mkdir __pypackages__
pdm install
pdm run gunicorn lunastarter.asgi:application -k uvicorn.workers.UvicornWorker
```

In your web browser go to: http://localhost:8000/graphql

Enter the query:

```graphql
subscription {
  countSeconds(upTo: 30)
}
```
