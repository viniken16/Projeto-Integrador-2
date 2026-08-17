import Link from "next/link";
import { getIndicatorsSummary } from "@/lib/api";

function formatPercent(value: number) {
  return `${value.toFixed(1)}%`;
}

function formatMoney(value: number) {
  return value.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

export default async function Home() {
  const indicators = await getIndicatorsSummary();

  return (
    <main className="mx-auto flex w-full max-w-5xl flex-1 flex-col gap-10 px-6 py-12">
      <section className="space-y-4">
        <p className="text-sm font-medium uppercase tracking-wide text-sky-800">
          Projeto Integrador II · UniCEUB
        </p>
        <h1 className="max-w-3xl text-4xl font-semibold tracking-tight text-slate-900">
          Uma plataforma simples para contratar e oferecer diárias com mais confiança.
        </h1>
        <p className="max-w-2xl text-lg leading-8 text-slate-600">
          No PI I o grupo mostrou informalidade, medo de calote e barreira de segurança no
          trabalho doméstico. Neste semestre o produto é o MVP: cadastro, pedido de diária e
          avaliação — sem pagamento, chat ou geolocalização avançada.
        </p>
        <div className="flex flex-wrap gap-3">
          <Link
            href="/cadastro/contratante"
            className="rounded-full bg-sky-800 px-5 py-2.5 text-sm font-medium text-white hover:bg-sky-900"
          >
            Quero contratar
          </Link>
          <Link
            href="/cadastro/diarista"
            className="rounded-full border border-slate-300 bg-white px-5 py-2.5 text-sm font-medium text-slate-800 hover:bg-slate-100"
          >
            Sou diarista
          </Link>
        </div>
      </section>

      <section className="grid gap-4 sm:grid-cols-3">
        <article className="rounded-2xl border border-slate-200 bg-white p-5">
          <p className="text-sm text-slate-500">Informalidade no trabalho doméstico</p>
          <p className="mt-2 text-3xl font-semibold text-slate-900">
            {indicators
              ? formatPercent(indicators.informalidade_domestica.informal)
              : "—"}
          </p>
          <p className="mt-1 text-sm text-slate-500">sem carteira (PNAD-C / PI I)</p>
        </article>
        <article className="rounded-2xl border border-slate-200 bg-white p-5">
          <p className="text-sm text-slate-500">Rendimento médio com carteira</p>
          <p className="mt-2 text-3xl font-semibold text-slate-900">
            {indicators ? formatMoney(indicators.rendimento_domestico.formal) : "—"}
          </p>
          <p className="mt-1 text-sm text-slate-500">trabalho doméstico formal</p>
        </article>
        <article className="rounded-2xl border border-slate-200 bg-white p-5">
          <p className="text-sm text-slate-500">Rendimento médio sem carteira</p>
          <p className="mt-2 text-3xl font-semibold text-slate-900">
            {indicators ? formatMoney(indicators.rendimento_domestico.informal) : "—"}
          </p>
          <p className="mt-1 text-sm text-slate-500">trabalho doméstico informal</p>
        </article>
      </section>

      <p className="text-sm text-slate-500">
        {indicators
          ? `Fonte: ${indicators.fonte}${indicators.periodo ? ` · ${indicators.periodo}` : ""}.`
          : "API de indicadores indisponível. Suba o FastAPI em localhost:8000 para ver os KPIs do PI I."}
      </p>
    </main>
  );
}
