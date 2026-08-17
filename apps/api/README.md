# API — Projeto Integrador II

FastAPI do MVP. Nesta etapa: `GET /health` e `GET /indicators/summary` (marts do PI I). Autenticação JWT e PostgreSQL entram no backlog do Módulo 4.

## Como rodar

```powershell
cd apps/api
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

- Health: http://localhost:8000/health
- Indicadores: http://localhost:8000/indicators/summary
- Docs: http://localhost:8000/docs

## Testes

```powershell
cd apps/api
python -m pytest
```

## Variáveis de ambiente

Copie `.env.example` para `.env` se precisar apontar os marts para outro diretório.
