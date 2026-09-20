---
name: saas-commercialization
description: Use this skill when the user wants to turn an existing product, prototype, API, open-source project, internal tool, or service into a commercially operable SaaS business, or wants a complete SaaS commercialization blueprint. It covers customer definition, offer design, pricing and revenue, payments and billing, SaaS platform capabilities, go-to-market, customer operations, finance, metrics, compliance, risks, and launch sequencing. Also use it to audit why an existing SaaS is not commercially ready. Do not use for a narrow feature implementation, a pitch deck alone, or generic startup ideation that does not require an operating SaaS plan.
---

# SaaS Commercialization

Turn a real product into a decision-ready, commercially operable SaaS plan. Produce a coherent operating system for the business, not a catalog of generic SaaS advice.

Respond in the user's language. Preserve their product, audience, geography, budget, technical stack, and business constraints. Do not silently replace the product concept.

## Select the operating mode

- **Full blueprint:** The user asks for a complete SaaS plan or to commercialize a product. Read all references linked below.
- **Commercial model:** Customer, positioning, packaging, pricing, revenue, or unit economics. Read [commercial-model.md](references/commercial-model.md) and, when calculations or targets matter, [finance-risk-and-metrics.md](references/finance-risk-and-metrics.md).
- **Platform readiness:** Accounts, tenants, entitlements, metering, onboarding, admin, security, or reliability. Read [product-platform.md](references/product-platform.md).
- **Payments and operations:** Checkout, subscriptions, invoices, tax handling, dunning, refunds, support, or back-office workflows. Read [payments-and-operations.md](references/payments-and-operations.md).
- **Launch and growth:** Acquisition, sales motion, activation, retention, lifecycle communication, or rollout. Read [go-to-market.md](references/go-to-market.md).
- **Readiness audit:** Evaluate an existing SaaS against the full blueprint, but focus the output on gaps, severity, evidence, and remediation order.

For a full blueprint, use [blueprint-template.md](references/blueprint-template.md) as the output contract.

## Ground the plan

Inspect the product materials the user provided: repository, live site, screenshots, requirements, current users, analytics, pricing, infrastructure, or support history. When access is available and the source is relevant, inspect it before recommending changes.

Establish four evidence classes:

1. **Known:** Directly supported by the user's materials or a cited source.
2. **Inferred:** A reasoned conclusion from known facts.
3. **Assumed:** A temporary input needed to complete the plan.
4. **Unknown:** Information whose absence materially changes a decision.

Attach provenance to material claims: user statement, product telemetry, financial record, contract, provider documentation, market source, or professional opinion. If current external facts cannot be verified, label them unverified and replace the missing conclusion with a concrete verification checklist and release gate.

Ask questions only when an unknown would change the target customer, business model, payment feasibility, regulatory posture, or implementation scope. Ask at most three high-leverage questions at once. Otherwise state reasonable assumptions and proceed.

When a full blueprint lacks enough evidence for a reliable final plan, deliver it in two stages:

- **Decision draft:** Recommended direction, explicit assumptions, reversible choices, blocking unknowns, and the fastest evidence plan.
- **Verified plan:** Updated pricing, provider selection, economics, compliance gates, and rollout commitments after the blocking evidence is collected.

Do not make a draft appear final merely because every template section has content.

Research current facts when recommendations depend on changing external conditions such as payment-provider availability, transaction fees, tax rules, privacy requirements, sanctions, platform terms, competitor pricing, or market conditions. Prefer primary sources. Label legal, tax, and accounting conclusions as issues requiring qualified review rather than presenting them as professional advice.

## Core workflow

### 1. Diagnose the product

Describe the current product, user problem, maturity, existing moat, dependencies, constraints, and the smallest commercial outcome it can reliably deliver. Separate the product's core value from features that merely make it look like a SaaS.

If the product has no plausible recurring value, do not force a subscription model. Recommend the best-fitting revenue model and explain the implication.

### 2. Choose the customer and buying motion

Define one primary ideal customer profile and one primary buyer. Distinguish user, buyer, approver, and beneficiary when they differ. Select the default motion—self-serve, sales-assisted, product-led, enterprise, marketplace, usage-led, or hybrid—based on deal size, implementation effort, trust burden, and buying complexity.

### 3. Design one coherent commercial offer

Recommend a primary positioning, promise, packaging model, value metric, pricing architecture, trial or proof mechanism, and expansion path. Provide one default recommendation; include an alternative only when a specific unresolved variable could reverse the choice.

Never invent willingness-to-pay as a precise fact. Use hypotheses, comparable evidence, or test ranges. Show what evidence would validate the price.

### 4. Define the commercial platform

Translate the offer into required SaaS capabilities: identity, tenancy, roles, onboarding, entitlements, metering, quotas, billing state, notifications, auditability, admin operations, security, observability, backup, export, deletion, and customer-facing status or support surfaces. Classify capabilities as **Launch blocker**, **Next**, or **Scale later**.

Classify launch blockers against the correct gate: **private paid pilot**, **public self-serve launch**, or **scale**. A capability may be manually controlled during a small pilot but mandatory before public self-service.

Do not recommend enterprise architecture for an unvalidated product unless the target buyer requires it.

### 5. Design money movement and revenue operations

Map the full order-to-cash lifecycle: acquisition source, signup or sales handoff, checkout or contract, payment authorization, provisioning, invoicing, tax evidence, renewal, failed payment, downgrade, cancellation, refund, dispute, reconciliation, and revenue reporting.

Recommend providers only after checking geography, supported business entity, settlement currency, customer location, sales channel, average order value, recurring billing needs, and compliance burden. Distinguish payment processor, merchant of record, billing engine, tax service, invoicing system, and accounting ledger.

Verify payment-provider acceptance, banking or payout acceptance, and upstream vendor or licensing permission independently. Approval from one does not imply approval from the others.

### 6. Build the operating model

Specify ownership and service levels for customer support, incidents, abuse, refunds, billing exceptions, onboarding, account recovery, data requests, vendor failures, and product feedback. Prefer workflows that a small team can actually run. Identify which operations are manual at launch and the threshold that justifies automation.

### 7. Build the growth and retention system

Choose channels based on where the primary buyer already searches, evaluates, and buys. Connect acquisition to activation, habitual value, retention, expansion, and referral. Avoid a channel list with no owner, asset, cadence, funnel stage, or success threshold.

### 8. Model viability

Show formulas and assumptions for revenue, gross margin, payment cost, infrastructure cost, support cost, customer acquisition cost, contribution margin, churn, LTV, payback, runway, and break-even where relevant. Use conservative/base/upside scenarios when inputs are uncertain. Never fabricate precision.

### 9. Sequence the launch

Create a prioritized roadmap with dependencies, owner roles, acceptance evidence, and exit criteria. A task is not complete because code exists; the customer must be able to discover, buy, receive, use, renew, obtain support for, and leave the service safely.

If the product already has customers, include a migration plan for accounts, balances, contracts or policy acceptance, entitlements, billing dates, historical data, support communications, reconciliation, and rollback.

### 10. Validate the blueprint

Before delivery, check:

- The customer, value metric, pricing, product entitlements, billing behavior, and metrics agree with each other.
- Every paid promise maps to a deliverable product capability and operating owner.
- The payment path works for the intended seller entity and buyer geography.
- Unit economics include payment, infrastructure, support, refund, and abuse costs.
- The roadmap distinguishes launch requirements from later scale work.
- Current claims have sources; assumptions and unresolved decisions are visible.
- Risks have triggers, mitigations, and owners rather than vague warnings.
- The final plan makes decisions. It does not merely offer menus.

If validation reveals a contradiction, fix the plan or flag a blocking decision before presenting it.

## Guardrails

- Do not perform purchases, create payment accounts, contact customers, publish pricing, accept contracts, deploy production changes, or alter live systems unless the user separately authorizes that action.
- Do not imply that incorporating a company, using a merchant of record, or adding policy pages alone makes the service compliant.
- Do not treat total signups, page views, or gross payment volume as proof of product-market fit.
- Do not bury the recommended direction beneath alternatives. Lead with the decision and its rationale.
- Do not make the plan look complete by adding unsupported market-size figures or invented competitor data.
- For regulated, high-risk, or geographically restricted products, add explicit legal, payments, abuse, and account-termination gates.

## Delivery standard

Lead with the commercial verdict and the few decisions that determine the rest of the plan. Use tables where they clarify pricing, responsibilities, economics, risks, or roadmap dependencies. Keep the main narrative decision-oriented; move calculations and detailed inventories into appendices when needed.

When the user wants implementation next, convert the approved blueprint into epics and acceptance criteria. Do not silently start implementation from an unapproved commercial plan.
