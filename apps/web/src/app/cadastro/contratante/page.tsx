export default function CadastroContratantePage() {
  return (
    <main className="mx-auto w-full max-w-xl flex-1 px-6 py-12">
      <h1 className="text-3xl font-semibold tracking-tight">Cadastro do contratante</h1>
      <p className="mt-3 text-slate-600">
        Placeholder do MVP. Em breve: dados de contato, endereço resumido e critérios de
        confiança na hora de solicitar uma diária.
      </p>
      <form className="mt-8 space-y-4 rounded-2xl border border-slate-200 bg-white p-6">
        <label className="block text-sm font-medium text-slate-700">
          Nome
          <input className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2" disabled placeholder="Em breve" />
        </label>
        <label className="block text-sm font-medium text-slate-700">
          Região da residência
          <input className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2" disabled placeholder="Brasília" />
        </label>
        <button
          type="button"
          disabled
          className="rounded-full bg-slate-300 px-5 py-2.5 text-sm font-medium text-slate-600"
        >
          Cadastro em breve
        </button>
      </form>
    </main>
  );
}
