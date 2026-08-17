# Sprint 0 — Setup do repositório PI II

**Objetivo:** deixar o GitHub e o esqueleto técnico prontos para as sprints de produto.

## Meta

O grupo consegue clonar o repositório, subir API e web, ler os documentos da ementa e puxar uma issue do backlog.

## Itens desta sprint

- Mover o PI I para `heritage/pi1/` sem reescrever o Streamlit
- README do PI II (propósito, stack, como rodar)
- Esqueleto FastAPI (`/health`, `/indicators/summary`)
- Esqueleto Next.js (landing, cadastros, pedidos mock)
- EAP, product backlog, visão arquitetural, personas e roteiro de stakeholders
- Templates de issue/PR, CI e milestones

## Definition of Done

- `uvicorn` responde em `/health`
- `pytest` da API passa
- `npm run build` do front passa (landing degrada se a API estiver fora)
- Documentos intermediários versionados em `docs/`
- Issues #1–#15 criadas nos milestones da ementa (board GitHub Project fica para a UI, por falta de escopo `project` no `gh`)

## Fora desta sprint

Auth JWT, PostgreSQL, CRUD de pedidos, Figma de alta fidelidade, deploy em nuvem.
