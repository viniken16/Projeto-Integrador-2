export type IndicatorKpi = {
  informal: number;
  formal: number;
};

export type RendimentoKpi = {
  formal: number;
  informal: number;
};

export type IndicatorsSummary = {
  fonte: string;
  periodo: string | null;
  informalidade_geral: IndicatorKpi;
  informalidade_domestica: IndicatorKpi;
  rendimento_domestico: RendimentoKpi;
};

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function getIndicatorsSummary(): Promise<IndicatorsSummary | null> {
  try {
    const response = await fetch(`${API_URL}/indicators/summary`, {
      cache: "no-store",
    });
    if (!response.ok) {
      return null;
    }
    return (await response.json()) as IndicatorsSummary;
  } catch {
    return null;
  }
}
