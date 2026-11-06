import os

assets_dir = r"C:\Users\Rahul Chaube\Downloads\design-patterns-for-humans-master\design-patterns-for-humans-master\assets"
os.makedirs(assets_dir, exist_ok=True)

# 4. structural-matrix.svg (1000 x 480)
structural_svg = """<svg width="1000" height="480" viewBox="0 0 1000 480" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sBg" x1="0" y1="0" x2="1000" y2="480" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0b0f19" />
      <stop offset="100%" stop-color="#0e1726" />
    </linearGradient>
    <pattern id="sGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#4338ca" fill-opacity="0.25" />
    </pattern>
  </defs>

  <rect width="1000" height="480" fill="url(#sBg)" rx="12" />
  <rect width="1000" height="480" fill="url(#sGrid)" rx="12" />
  <rect width="998" height="478" x="1" y="1" rx="11" stroke="#312e81" stroke-width="1.5" stroke-opacity="0.6" fill="none" />

  <!-- Header -->
  <g transform="translate(40, 36)">
    <text x="0" y="0" fill="#818cf8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" letter-spacing="1">STRUCTURAL BLUEPRINT</text>
    <text x="0" y="28" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800">Structural Patterns Architectural Matrix</text>
    <text x="0" y="50" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5">Organizing class and object composition to assemble scalable, loosely-coupled architectures.</text>
  </g>

  <!-- Table Headers -->
  <g transform="translate(40, 105)">
    <rect width="920" height="34" rx="6" fill="#1e1b4b" />
    <text x="20" y="22" fill="#a5b4fc" font-family="monospace" font-size="12" font-weight="700">PATTERN</text>
    <text x="180" y="22" fill="#a5b4fc" font-family="monospace" font-size="12" font-weight="700">STRUCTURAL INTENT</text>
    <text x="490" y="22" fill="#a5b4fc" font-family="monospace" font-size="12" font-weight="700">REAL-WORLD APPLICATION</text>
    <text x="770" y="22" fill="#a5b4fc" font-family="monospace" font-size="12" font-weight="700">DISTINGUISHING TRAIT</text>
  </g>

  <!-- Row 1: Adapter -->
  <g transform="translate(40, 147)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#818cf8" font-family="monospace" font-size="12.5" font-weight="700">Adapter</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Converts incompatible interface</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Payment gateways (Stripe vs PayPal)</text>
    <text x="770" y="26" fill="#38bdf8" font-family="monospace" font-size="11.5">Changes interface</text>
  </g>

  <!-- Row 2: Bridge -->
  <g transform="translate(40, 193)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#818cf8" font-family="monospace" font-size="12.5" font-weight="700">Bridge</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Decouples abstraction from implementation</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Cross-platform UI (Theme x Platform)</text>
    <text x="770" y="26" fill="#38bdf8" font-family="monospace" font-size="11.5">Dual hierarchies</text>
  </g>

  <!-- Row 3: Composite -->
  <g transform="translate(40, 239)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#818cf8" font-family="monospace" font-size="12.5" font-weight="700">Composite</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Treats leaf and composite uniformly</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">File systems, DOM trees, UI widgets</text>
    <text x="770" y="26" fill="#38bdf8" font-family="monospace" font-size="11.5">Recursive tree</text>
  </g>

  <!-- Row 4: Decorator -->
  <g transform="translate(40, 285)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#818cf8" font-family="monospace" font-size="12.5" font-weight="700">Decorator</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Dynamic runtime behavioral augmentation</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">HTTP middlewares, I/O streams</text>
    <text x="770" y="26" fill="#38bdf8" font-family="monospace" font-size="11.5">Preserves interface</text>
  </g>

  <!-- Row 5: Facade -->
  <g transform="translate(40, 331)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#818cf8" font-family="monospace" font-size="12.5" font-weight="700">Facade</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Unified entry point to complex subsystem</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Order checkout (Cart + Billing + Mail)</text>
    <text x="770" y="26" fill="#38bdf8" font-family="monospace" font-size="11.5">Simplifies subsystem</text>
  </g>

  <!-- Row 6: Flyweight & Proxy -->
  <g transform="translate(40, 377)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#818cf8" font-family="monospace" font-size="12.5" font-weight="700">Flyweight / Proxy</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">State sharing / Controlled access surrogate</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Game particle rendering / Lazy loading</text>
    <text x="770" y="26" fill="#38bdf8" font-family="monospace" font-size="11.5">Efficiency &amp; Control</text>
  </g>

  <g transform="translate(40, 440)">
    <circle cx="6" cy="6" r="3" fill="#818cf8" />
    <text x="16" y="10" fill="#64748b" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Architectural Comparison: Decorator enhances what an object does; Adapter changes how it looks; Proxy controls access to it.</text>
  </g>
</svg>"""

with open(os.path.join(assets_dir, "structural-matrix.svg"), "w", encoding="utf-8") as f:
    f.write(structural_svg)

# 5. behavioral-matrix.svg (1000 x 480)
behavioral_svg = """<svg width="1000" height="480" viewBox="0 0 1000 480" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bBg" x1="0" y1="0" x2="1000" y2="480" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#061210" />
      <stop offset="100%" stop-color="#0b1b17" />
    </linearGradient>
    <pattern id="bGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#047857" fill-opacity="0.3" />
    </pattern>
  </defs>

  <rect width="1000" height="480" fill="url(#bBg)" rx="12" />
  <rect width="1000" height="480" fill="url(#bGrid)" rx="12" />
  <rect width="998" height="478" x="1" y="1" rx="11" stroke="#065f46" stroke-width="1.5" stroke-opacity="0.6" fill="none" />

  <!-- Header -->
  <g transform="translate(40, 36)">
    <text x="0" y="0" fill="#34d399" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" letter-spacing="1">BEHAVIORAL BLUEPRINT</text>
    <text x="0" y="28" fill="#f8fafc" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800">Behavioral Patterns Architectural Matrix</text>
    <text x="0" y="50" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5">Managing communication, algorithm assignment, execution pipelines, and state transitions.</text>
  </g>

  <!-- Table Headers -->
  <g transform="translate(40, 105)">
    <rect width="920" height="34" rx="6" fill="#064e3b" />
    <text x="20" y="22" fill="#a7f3d0" font-family="monospace" font-size="12" font-weight="700">PATTERN</text>
    <text x="180" y="22" fill="#a7f3d0" font-family="monospace" font-size="12" font-weight="700">BEHAVIORAL FOCUS</text>
    <text x="490" y="22" fill="#a7f3d0" font-family="monospace" font-size="12" font-weight="700">CORE USE CASE</text>
    <text x="770" y="22" fill="#a7f3d0" font-family="monospace" font-size="12" font-weight="700">KEY ARCHITECTURAL ADVANTAGE</text>
  </g>

  <!-- Row 1: Chain of Responsibility -->
  <g transform="translate(40, 147)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#34d399" font-family="monospace" font-size="12.5" font-weight="700">Chain of Resp.</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Sequential request handling</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Auth filters, validation pipelines</text>
    <text x="770" y="26" fill="#6ee7b7" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Decouples sender from handler</text>
  </g>

  <!-- Row 2: Command -->
  <g transform="translate(40, 193)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#34d399" font-family="monospace" font-size="12.5" font-weight="700">Command</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Encapsulates actions as standalone objects</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Undo/redo queues, asynchronous jobs</text>
    <text x="770" y="26" fill="#6ee7b7" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Parameterizes &amp; delays execution</text>
  </g>

  <!-- Row 3: Observer -->
  <g transform="translate(40, 239)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#34d399" font-family="monospace" font-size="12.5" font-weight="700">Observer</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">One-to-many subscription &amp; broadcast</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Event buses, reactive UI updates</text>
    <text x="770" y="26" fill="#6ee7b7" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Loose coupling via events</text>
  </g>

  <!-- Row 4: Strategy -->
  <g transform="translate(40, 285)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#34d399" font-family="monospace" font-size="12.5" font-weight="700">Strategy</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Family of interchangeable algorithms</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Sorting algorithms, pricing engines</text>
    <text x="770" y="26" fill="#6ee7b7" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Replaces complex conditionals</text>
  </g>

  <!-- Row 5: State -->
  <g transform="translate(40, 331)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#34d399" font-family="monospace" font-size="12.5" font-weight="700">State</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Behavior alters as internal state changes</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Order states (Pending, Paid, Shipped)</text>
    <text x="770" y="26" fill="#6ee7b7" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Eliminates nested switch/case</text>
  </g>

  <!-- Row 6: Template Method & Mediator -->
  <g transform="translate(40, 377)">
    <rect width="920" height="42" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="20" y="26" fill="#34d399" font-family="monospace" font-size="12.5" font-weight="700">Template / Mediator</text>
    <text x="180" y="26" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5">Algorithm skeleton / Centralized communication</text>
    <text x="490" y="26" fill="#cbd5e1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">CI/CD pipelines / Chat rooms, Air traffic</text>
    <text x="770" y="26" fill="#6ee7b7" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Enforces order &amp; reduces many-to-many</text>
  </g>

  <g transform="translate(40, 440)">
    <circle cx="6" cy="6" r="3" fill="#34d399" />
    <text x="16" y="10" fill="#64748b" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Architectural Comparison: Strategy swaps algorithm from outside; State transitions behavior internally; Template Method freezes the skeleton.</text>
  </g>
</svg>"""

with open(os.path.join(assets_dir, "behavioral-matrix.svg"), "w", encoding="utf-8") as f:
    f.write(behavioral_svg)

print("Generated all 5 visual assets successfully!")
