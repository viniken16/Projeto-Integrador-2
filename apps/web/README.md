# Front-end — Projeto Integrador II

Next.js (App Router) do MVP. Páginas desta etapa: landing com KPIs do PI I, cadastros placeholder e lista mock de pedidos.

## Como rodar

Na raiz do repositório, suba a API primeiro (`apps/api`). Depois:

```powershell
cd apps/web
copy .env.example .env.local
npm install
npm run dev
```

Abra http://localhost:3000

## Scripts

- `npm run dev` — desenvolvimento
- `npm run build` — build de produção (CI)
- `npm run lint` — ESLint
