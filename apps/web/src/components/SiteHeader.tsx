import Link from "next/link";

const links = [
  { href: "/", label: "Início" },
  { href: "/cadastro/diarista", label: "Sou diarista" },
  { href: "/cadastro/contratante", label: "Quero contratar" },
  { href: "/pedidos", label: "Pedidos" },
];

export function SiteHeader() {
  return (
    <header className="border-b border-slate-200 bg-white">
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-4 px-6 py-4">
        <Link href="/" className="text-sm font-semibold tracking-tight text-slate-900">
          Diárias com confiança
        </Link>
        <nav className="flex flex-wrap items-center gap-3 text-sm text-slate-600">
          {links.map((link) => (
            <Link key={link.href} href={link.href} className="hover:text-slate-900">
              {link.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
