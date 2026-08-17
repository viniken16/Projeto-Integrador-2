# Product backlog — PI II

Épicos e histórias iniciais do MVP. Issues no GitHub: [viniken16/Projeto-Integrador-2/issues](https://github.com/viniken16/Projeto-Integrador-2/issues). Milestones seguem os módulos da ementa.

**Fora do MVP:** pagamento, chat, geolocalização avançada, matching automático por algoritmo.

## Épico A — Confiança e perfil

Como diarista ou contratante, quero um cadastro com sinais de confiança para reduzir medo de calote, assédio e “desconhecido em casa”.

- A1. Cadastro da diarista com região, bio e indicação de verificação — [#5](https://github.com/viniken16/Projeto-Integrador-2/issues/5)
- A2. Cadastro do contratante com região da residência — [#6](https://github.com/viniken16/Projeto-Integrador-2/issues/6)
- A3. Perfil público resumido (avaliação média quando existir) — [#9](https://github.com/viniken16/Projeto-Integrador-2/issues/9)

## Épico B — Matching de pedidos

Como contratante, quero solicitar uma diária. Como diarista, quero aceitar ou recusar.

- B1–B4. Pedidos (criar, listar, aceitar/recusar, status) — [#7](https://github.com/viniken16/Projeto-Integrador-2/issues/7) e [#10](https://github.com/viniken16/Projeto-Integrador-2/issues/10)

## Épico C — Avaliação pós-serviço

Como usuária, quero avaliar a diária para construir reputação e reduzir informalidade relacional.

- C1–C2. Conclusão e avaliação — [#11](https://github.com/viniken16/Projeto-Integrador-2/issues/11)

## Épico D — Indicadores e vínculo com o PI I

Como visitante, quero ver o tamanho do problema (informalidade e rendimento) na landing.

- D1. API `GET /indicators/summary` a partir dos marts (esqueleto na Sprint 0)
- D2. Cards de KPI na home — [#4](https://github.com/viniken16/Projeto-Integrador-2/issues/4)

## Épico E — Qualidade e operação

- E1. Testes unitários da API — [#13](https://github.com/viniken16/Projeto-Integrador-2/issues/13)
- E2. Testes de integração (API + persistência, quando existir) — [#12](https://github.com/viniken16/Projeto-Integrador-2/issues/12)
- E3. Testes de aceitação do fluxo solicitar/aceitar — [#14](https://github.com/viniken16/Projeto-Integrador-2/issues/14)
- E4. CI no GitHub Actions (esqueleto na Sprint 0)

## Prioridade sugerida (MoSCoW)

- Must: A1, A2, B1, B2, B3, D1, D2, E1
- Should: B4, C1, C2, E3
- Could: A3, E2, E4
- Won't (neste semestre): pagamento, chat, GPS
