# Projeto Integrador II

**Tema:** MVP de plataforma para conectar diaristas e contratantes, com foco em confiança, segurança e trabalho decente (ODS 8).

**Repositório:** [https://github.com/viniken16/Projeto-Integrador-2](https://github.com/viniken16/Projeto-Integrador-2)

## Diferença em relação ao PI I

No PI I o grupo explorou o espaço do problema: informalidade no serviço de limpeza doméstica, pesquisa de campo, ETL da PNAD-C e dashboard Streamlit. A entrega era evidência de que o problema existe.

No PI II o foco é o **produto**: um site dinâmico (Next.js + FastAPI) em que diarista e contratante se cadastram, pedem/aceitam uma diária e avaliam o serviço. Os marts do PI I entram como indicadores na landing — não substituem a plataforma.

O legado do semestre anterior está em [`heritage/pi1/`](heritage/pi1/README.md). Dashboard histórico: [https://pi-trabalho-domestico.streamlit.app](https://pi-trabalho-domestico.streamlit.app)

## Stack

- Front-end: Next.js (App Router) em `apps/web`
- Back-end: FastAPI em `apps/api`
- Indicadores: CSVs versionados do PI I (`GET /indicators/summary`)
- Persistência e JWT: documentados na arquitetura; implementação no backlog do Módulo 4

## Como rodar

Terminal 1 — API:

```powershell
cd apps/api
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Terminal 2 — Web:

```powershell
cd apps/web
copy .env.example .env.local
npm install
npm run dev
```

- App: http://localhost:3000
- API: http://localhost:8000/docs

## Quadro ágil no GitHub

- Issues: [github.com/viniken16/Projeto-Integrador-2/issues](https://github.com/viniken16/Projeto-Integrador-2/issues)
- Milestones: Sprint 0, Módulos 1–2, Módulo 3, Módulo 4, Módulo 5
- Labels: `historia`, `bug`, `spike`, `stakeholder`, `modulo-1-ux` … `modulo-5-qualidade`

Para um board (Backlog / Sprint / Em andamento / Review / Done), crie um GitHub Project na UI do repositório. O token local do `gh` não tem o escopo `project`; se quiser criar pela CLI: `gh auth refresh -s project,read:project`.

## Entregáveis intermediários (ementa)

- [EAP / WBS](docs/gestao/eap.md)
- [Product backlog](docs/gestao/product-backlog.md)
- [Sprint 0](docs/gestao/sprint-0.md)
- [Visão arquitetural](docs/arquitetura/visao-arquitetural.md)
- [Personas](docs/ux/personas.md)
- [Roteiro de entrevistas](docs/stakeholders/roteiro-entrevista.md)

## Estrutura

```text
Projeto-Integrador-2/
  apps/web/              Next.js
  apps/api/              FastAPI
  docs/gestao/           EAP, backlog, sprints
  docs/arquitetura/
  docs/ux/
  docs/stakeholders/
  docs/divulgacao/
  heritage/pi1/          pesquisa, ETL e dashboard do PI I
  tests/e2e/             aceitação (placeholder)
  .github/               issues, PR e CI
```

## Equipe

| Nome | Papel |
| --- | --- |
| Lucas Gonçalves | Product Owner |
| João Victor Rios | Desenvolvedor full-stack |
| Alexsander Motta | Analista de BI |
| Beatriz Vasconcellos | Pesquisadora UX |
| Vinicius Inoue | Analista de qualidade |

Parceria estratégica: SEBRAE. Orientação: professor da disciplina.

## Fora do MVP

Pagamento, chat, geolocalização avançada e reescrita do Streamlit.
