const mockPedidos = [
  { id: "1", data: "22/08/2026", status: "Pendente", papel: "Contratante" },
  { id: "2", data: "18/08/2026", status: "Aceito", papel: "Diarista" },
];

export default function PedidosPage() {
  return (
    <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-12">
      <h1 className="text-3xl font-semibold tracking-tight">Pedidos</h1>
      <p className="mt-3 text-slate-600">
        Área logada mockada. Sem autenticação nesta etapa. A lista real de solicitar / aceitar /
        recusar diária entra no backlog de front e back.
      </p>
      <ul className="mt-8 space-y-3">
        {mockPedidos.map((pedido) => (
          <li
            key={pedido.id}
            className="flex items-center justify-between rounded-2xl border border-slate-200 bg-white px-5 py-4"
          >
            <div>
              <p className="font-medium text-slate-900">Diária #{pedido.id}</p>
              <p className="text-sm text-slate-500">
                {pedido.data} · visão {pedido.papel}
              </p>
            </div>
            <span className="rounded-full bg-slate-100 px-3 py-1 text-sm text-slate-700">
              {pedido.status}
            </span>
          </li>
        ))}
      </ul>
    </main>
  );
}
