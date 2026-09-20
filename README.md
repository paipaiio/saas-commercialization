# SaaS Commercialization Skill

Turn an existing product, API, prototype, open-source project, internal tool, or service into a commercially operable SaaS plan.

This Agent Skill produces a decision-ready commercialization blueprint that connects the business model to the product and operating system required to deliver it. It covers customers, positioning, pricing, billing, payments, entitlements, metering, go-to-market, support, finance, metrics, compliance, risk, and phased launch execution.

## What makes it different

- Starts with a commercial verdict instead of a generic feature list.
- Separates known facts, inferences, assumptions, and blocking unknowns.
- Maps every paid promise through entitlement, product behavior, metering, billing state, customer visibility, and support operations.
- Distinguishes payment processors, merchants of record, billing engines, tax services, accounting systems, banks, and upstream licensing.
- Uses a decision draft when evidence is incomplete, then defines what is needed for a verified plan.
- Separates private paid pilot, public self-serve launch, and scale gates.
- Produces conservative, base, and upside economics without inventing precision.

## Install

Install with the Agent Skills CLI:

```bash
npx skills add paipaiio/saas-commercialization
```

Or clone it into your agent's skill directory:

```bash
git clone https://github.com/paipaiio/saas-commercialization.git ~/.codex/skills/saas-commercialization
```

Common skill directories include:

- OpenAI Codex: `~/.codex/skills/`
- Claude Code: `~/.claude/skills/`
- Cursor: `.cursor/skills/`
- GitHub Copilot: `.github/skills/`

## Use

The skill can activate automatically for SaaS commercialization requests. You can also invoke it explicitly:

```text
Use $saas-commercialization to inspect this product and produce a complete SaaS commercialization blueprint.
```

Examples:

```text
Turn this open-source API gateway into a revenue-ready SaaS.
```

```text
Audit whether this product is ready for paid self-service customers.
```

```text
Design the pricing, billing, payments, customer operations, and 90-day launch plan for this product.
```

The output follows the user's language.

## Repository structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── blueprint-template.md
│   ├── commercial-model.md
│   ├── finance-risk-and-metrics.md
│   ├── go-to-market.md
│   ├── payments-and-operations.md
│   └── product-platform.md
└── tests/
    └── test_skill_structure.py
```

`SKILL.md` contains routing, evidence rules, the core workflow, and guardrails. Detailed domain guidance is loaded from `references/` only when relevant.

## Scope

Use this skill for full SaaS commercialization or commercial-readiness audits. It is not intended for narrow feature implementation, standalone pitch decks, or generic startup ideation without an operating SaaS plan.

Recommendations involving current provider availability, fees, laws, taxes, sanctions, or platform terms must be verified against current primary sources. Legal, tax, and accounting matters require qualified review.

## Validation

The repository includes automated checks for Agent Skills metadata, reference integrity, UI metadata, unfinished placeholders, and entrypoint size:

```bash
python -m unittest discover -s tests -v
```

## License

MIT
