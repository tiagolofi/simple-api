# simple-api

Um provedor de APIs baseado em arquivos de configuração

# How to use

1. Configure um arquivo de configurações com o nome `simple-api.yaml`:

```yaml
routes:  
  - path: /greeting
    package: example
    method: POST
    request: GreetingRequest
    response: GreetingResponse
    handler: handler_fn

auth: null # dados de autenticação
```

2. Crie um pacote com a implementação concreta com o seguinte formato

- `projeto`
```markdown
app.py
example/
    __init__.py
    greeting.py
```

- `__init__.py`
```python
from example.greeting import GreetingRequest, GreetingResponse, handler_fn
```

- `greeting.py`
```python
from sapi.core.models import Request, Response

class GreetingRequest(Request):
    ...

class GreetingResponse(Response):
    greeting: str

def handler_fn(request: GreetingRequest) -> GreetingResponse:
    res = GreetingResponse(id = request.id, greeting = "Olá Mundo")
    return res
```

- `app.py`
```python
from sapi.core import SimpleApi, Managers

yaml_manager = Managers.YAML # gerencia o arquivo, também disponível para .json

app = SimpleApi(yaml_manager)
```

3. Execute: `uvicorn app:app --reload`

Obs: este pacote abstrai autenticação e frameworks web, garantindo que o desenvolvedor foque apenas na solução a ser entregue.