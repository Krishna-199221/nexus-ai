const stats = [
  {
    label: "Sources Connected",
    value: "12",
    detail: "+3 this week",
  },
  {
    label: "Documents Processed",
    value: "47",
    detail: "All systems ready",
  },
  {
    label: "Insights Discovered",
    value: "23",
    detail: "8 high priority",
  },
  {
    label: "Optimization Opportunities",
    value: "9",
    detail: "3 need attention",
  },
];

const insights = [
  {
    title: "Resource utilization imbalance detected",
    description:
      "Several resources show significant differences between available capacity and current utilization.",
    type: "Optimization",
    priority: "High",
  },
  {
    title: "Potential process bottleneck identified",
    description:
      "Recent operational records indicate a recurring delay around resource allocation.",
    type: "Risk",
    priority: "Medium",
  },
  {
    title: "Underutilized capacity available",
    description:
      "Available capacity could potentially be reassigned to higher-demand activities.",
    type: "Opportunity",
    priority: "Medium",
  },
];

const sources = [
  {
    name: "Resource Utilization Report",
    type: "PDF",
    status: "Processed",
  },
  {
    name: "Operational Records",
    type: "CSV",
    status: "Processed",
  },
  {
    name: "Department Guidelines",
    type: "DOCX",
    status: "Processed",
  },
  {
    name: "External Information",
    type: "Web",
    status: "Connected",
  },
];

export default function Home() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="flex min-h-screen">
        {/* Sidebar */}
        <aside className="hidden w-64 shrink-0 border-r border-slate-800 bg-slate-950 lg:flex lg:flex-col">
          <div className="flex h-20 items-center border-b border-slate-800 px-6">
            <div>
              <p className="text-xl font-bold tracking-tight text-white">
                NEXUS <span className="text-cyan-400">AI</span>
              </p>
              <p className="mt-0.5 text-xs text-slate-500">
                Resource Intelligence
              </p>
            </div>
          </div>

          <nav className="flex-1 space-y-1 px-3 py-6">
            <SidebarItem icon="⌂" label="Dashboard" active />
            <SidebarItem icon="◈" label="Sources" />
            <SidebarItem icon="✦" label="AI Assistant" />
            <SidebarItem icon="◎" label="Insights" />
            <SidebarItem icon="▣" label="Resources" />
            <SidebarItem icon="↗" label="Workflows" />
          </nav>

          <div className="border-t border-slate-800 p-4">
            <div className="rounded-xl border border-slate-800 bg-slate-900 p-4">
              <p className="text-xs font-medium text-slate-500">
                SYSTEM STATUS
              </p>
              <div className="mt-3 flex items-center gap-2">
                <span className="h-2 w-2 rounded-full bg-emerald-400" />
                <span className="text-sm text-slate-300">All systems operational</span>
              </div>
            </div>
          </div>
        </aside>

        {/* Main */}
        <main className="min-w-0 flex-1">
          {/* Top bar */}
          <header className="flex h-20 items-center justify-between border-b border-slate-800 bg-slate-950/90 px-6 lg:px-10">
            <div>
              <p className="text-sm text-slate-500">Workspace</p>
              <h1 className="text-lg font-semibold text-white">
                Resource Intelligence
              </h1>
            </div>

            <div className="flex items-center gap-3">
              <button className="hidden rounded-lg border border-slate-700 px-4 py-2 text-sm font-medium text-slate-300 transition hover:border-slate-600 hover:bg-slate-900 sm:block">
                Generate Report
              </button>

              <div className="flex h-9 w-9 items-center justify-center rounded-full bg-cyan-400 text-sm font-bold text-slate-950">
                K
              </div>
            </div>
          </header>

          <div className="mx-auto max-w-7xl px-6 py-8 lg:px-10">
            {/* Hero */}
            <section className="mb-8">
              <div className="rounded-2xl border border-slate-800 bg-gradient-to-br from-slate-900 to-slate-950 p-7">
                <div className="max-w-3xl">
                  <div className="mb-3 inline-flex items-center gap-2 rounded-full border border-cyan-400/20 bg-cyan-400/10 px-3 py-1 text-xs font-medium text-cyan-300">
                    <span className="h-1.5 w-1.5 rounded-full bg-cyan-400" />
                    AI RESOURCE INTELLIGENCE
                  </div>

                  <h2 className="text-3xl font-bold tracking-tight text-white md:text-4xl">
                    Turn scattered information into{" "}
                    <span className="text-cyan-400">actionable decisions.</span>
                  </h2>

                  <p className="mt-4 max-w-2xl text-sm leading-6 text-slate-400 md:text-base">
                    NEXUS AI connects your information sources, understands
                    their contents, discovers important insights, and helps
                    transform them into optimized actions.
                  </p>

                  <div className="mt-6 flex flex-wrap gap-3">
                    <button className="rounded-lg bg-cyan-400 px-5 py-2.5 text-sm font-semibold text-slate-950 transition hover:bg-cyan-300">
                      + Add Source
                    </button>
                    <button className="rounded-lg border border-slate-700 px-5 py-2.5 text-sm font-semibold text-slate-300 transition hover:bg-slate-800">
                      Ask AI
                    </button>
                  </div>
                </div>
              </div>
            </section>

            {/* Metrics */}
            <section className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
              {stats.map((stat) => (
                <div
                  key={stat.label}
                  className="rounded-xl border border-slate-800 bg-slate-900 p-5"
                >
                  <p className="text-sm text-slate-500">{stat.label}</p>
                  <div className="mt-3 flex items-end justify-between gap-3">
                    <p className="text-3xl font-bold text-white">
                      {stat.value}
                    </p>
                    <span className="text-xs text-emerald-400">
                      {stat.detail}
                    </span>
                  </div>
                </div>
              ))}
            </section>

            {/* Main dashboard grid */}
            <section className="mt-6 grid gap-6 xl:grid-cols-3">
              {/* Insights */}
              <div className="xl:col-span-2 rounded-xl border border-slate-800 bg-slate-900">
                <div className="flex items-center justify-between border-b border-slate-800 px-6 py-5">
                  <div>
                    <h3 className="font-semibold text-white">
                      AI Insights
                    </h3>
                    <p className="mt-1 text-xs text-slate-500">
                      Findings generated from connected sources
                    </p>
                  </div>

                  <button className="text-xs font-medium text-cyan-400 hover:text-cyan-300">
                    View all
                  </button>
                </div>

                <div className="divide-y divide-slate-800">
                  {insights.map((insight) => (
                    <div key={insight.title} className="p-6">
                      <div className="flex flex-wrap items-center gap-2">
                        <span className="rounded-md bg-slate-800 px-2 py-1 text-[11px] font-medium text-slate-300">
                          {insight.type}
                        </span>

                        <span
                          className={`rounded-md px-2 py-1 text-[11px] font-medium ${
                            insight.priority === "High"
                              ? "bg-rose-400/10 text-rose-300"
                              : "bg-amber-400/10 text-amber-300"
                          }`}
                        >
                          {insight.priority} priority
                        </span>
                      </div>

                      <h4 className="mt-3 font-medium text-white">
                        {insight.title}
                      </h4>

                      <p className="mt-2 text-sm leading-6 text-slate-400">
                        {insight.description}
                      </p>

                      <button className="mt-4 text-xs font-medium text-cyan-400 hover:text-cyan-300">
                        Investigate insight →
                      </button>
                    </div>
                  ))}
                </div>
              </div>

              {/* Resource overview */}
              <div className="rounded-xl border border-slate-800 bg-slate-900">
                <div className="border-b border-slate-800 px-6 py-5">
                  <h3 className="font-semibold text-white">
                    Resource Overview
                  </h3>
                  <p className="mt-1 text-xs text-slate-500">
                    Current utilization snapshot
                  </p>
                </div>

                <div className="space-y-6 p-6">
                  <ResourceBar
                    label="People"
                    value="78%"
                    percentage={78}
                  />
                  <ResourceBar
                    label="Technology"
                    value="64%"
                    percentage={64}
                  />
                  <ResourceBar
                    label="Information"
                    value="86%"
                    percentage={86}
                  />
                  <ResourceBar
                    label="Time"
                    value="71%"
                    percentage={71}
                  />
                </div>

                <div className="border-t border-slate-800 p-6">
                  <button className="w-full rounded-lg border border-slate-700 py-2.5 text-sm font-medium text-slate-300 transition hover:bg-slate-800">
                    Analyze Resources
                  </button>
                </div>
              </div>
            </section>

            {/* Sources */}
            <section className="mt-6 rounded-xl border border-slate-800 bg-slate-900">
              <div className="flex items-center justify-between border-b border-slate-800 px-6 py-5">
                <div>
                  <h3 className="font-semibold text-white">
                    Connected Sources
                  </h3>
                  <p className="mt-1 text-xs text-slate-500">
                    Information currently available to NEXUS AI
                  </p>
                </div>

                <button className="rounded-lg border border-slate-700 px-3 py-2 text-xs font-medium text-slate-300 hover:bg-slate-800">
                  Manage sources
                </button>
              </div>

              <div className="grid gap-px bg-slate-800 md:grid-cols-2">
                {sources.map((source) => (
                  <div
                    key={source.name}
                    className="flex items-center justify-between bg-slate-900 p-5"
                  >
                    <div className="flex items-center gap-4">
                      <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-slate-800 text-xs font-bold text-cyan-400">
                        {source.type}
                      </div>

                      <div>
                        <p className="text-sm font-medium text-slate-200">
                          {source.name}
                        </p>
                        <p className="mt-1 text-xs text-slate-500">
                          {source.type} source
                        </p>
                      </div>
                    </div>

                    <span className="rounded-full bg-emerald-400/10 px-2.5 py-1 text-[11px] font-medium text-emerald-300">
                      {source.status}
                    </span>
                  </div>
                ))}
              </div>
            </section>

            {/* AI pipeline */}
            <section className="mt-6 rounded-xl border border-slate-800 bg-slate-900 p-6">
              <div className="mb-6">
                <h3 className="font-semibold text-white">
                  NEXUS Intelligence Pipeline
                </h3>
                <p className="mt-1 text-xs text-slate-500">
                  How information moves through the platform
                </p>
              </div>

              <div className="grid gap-3 md:grid-cols-6">
                {[
                  "Sources",
                  "Processing",
                  "Knowledge",
                  "AI Analysis",
                  "Insights",
                  "Automation",
                ].map((step, index) => (
                  <div key={step} className="flex items-center">
                    <div className="w-full rounded-lg border border-slate-700 bg-slate-950 p-4 text-center">
                      <div className="mx-auto mb-2 flex h-7 w-7 items-center justify-center rounded-full bg-cyan-400/10 text-xs font-bold text-cyan-400">
                        {index + 1}
                      </div>
                      <p className="text-xs font-medium text-slate-300">
                        {step}
                      </p>
                    </div>

                    {index < 5 && (
                      <span className="hidden px-2 text-slate-600 md:block">
                        →
                      </span>
                    )}
                  </div>
                ))}
              </div>
            </section>

            <footer className="py-8 text-center text-xs text-slate-600">
              NEXUS AI · AI-Powered Resource Intelligence & Automation Platform
            </footer>
          </div>
        </main>
      </div>
    </div>
  );
}

function SidebarItem({
  icon,
  label,
  active = false,
}: {
  icon: string;
  label: string;
  active?: boolean;
}) {
  return (
    <button
      className={`flex w-full items-center gap-3 rounded-lg px-4 py-3 text-sm transition ${
        active
          ? "bg-cyan-400/10 font-medium text-cyan-300"
          : "text-slate-400 hover:bg-slate-900 hover:text-slate-200"
      }`}
    >
      <span className="flex h-5 w-5 items-center justify-center text-base">
        {icon}
      </span>
      {label}
    </button>
  );
}

function ResourceBar({
  label,
  value,
  percentage,
}: {
  label: string;
  value: string;
  percentage: number;
}) {
  return (
    <div>
      <div className="mb-2 flex items-center justify-between">
        <span className="text-sm text-slate-300">{label}</span>
        <span className="text-xs font-medium text-slate-400">{value}</span>
      </div>

      <div className="h-2 overflow-hidden rounded-full bg-slate-800">
        <div
          className="h-full rounded-full bg-cyan-400"
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  );
}