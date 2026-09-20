# Finance, metrics, and risk

Read this reference for viability modeling, KPI design, scenarios, risk registers, compliance gates, and management cadence.

## Core formulas

Use consistent periods and state whether values are recognized revenue, billings, cash collected, or gross payment volume.

```text
MRR = sum of normalized recurring monthly subscription revenue
ARR = MRR × 12
Gross margin = (Revenue - cost of revenue) / Revenue
Contribution margin = Revenue - variable infrastructure - payment fees - variable support - refunds - fraud/abuse loss
Logo churn = customers lost during period / customers at period start
Revenue churn = recurring revenue lost during period / recurring revenue at period start
NRR = (starting recurring revenue - churn - contraction + expansion) / starting recurring revenue
ARPA = recurring revenue / average active paying accounts
CAC = attributable sales and marketing cost / new paying customers
CAC payback months = CAC / monthly gross profit per new customer
Simple LTV = ARPA × gross margin / monthly revenue churn
Break-even customers = monthly fixed costs / monthly contribution per customer
Runway months = available cash / average monthly net cash burn
```

State limitations. Do not use a simple infinite-horizon LTV when churn is unstable, cohorts are young, or expansion dominates.

## Cost model

Include relevant costs rather than hiding them in a generic infrastructure line:

- model, compute, storage, bandwidth, and third-party API consumption;
- payment fees, currency conversion, disputes, refunds, and merchant-of-record fees;
- customer onboarding and support labor;
- monitoring, security, email, analytics, and other production vendors;
- sales commissions and partner revenue share;
- tax or compliance operations;
- abuse, free-tier, promotional-credit, and failed-payment leakage.

Separate cost of revenue, operating expenses, one-time setup, and founder labor when possible.

## Scenario model

When inputs are uncertain, produce conservative, base, and upside cases. At minimum vary:

- traffic or qualified leads;
- conversion to paid;
- average selling price or usage;
- gross margin;
- churn and expansion;
- acquisition cost;
- support load;
- refund/fraud rate.

Explain which variable most affects viability and what evidence can reduce that uncertainty fastest.

## Metric tree

Choose a north-star measure representing delivered customer value. Connect it to:

- acquisition quality;
- activation;
- recurring core-value behavior;
- retention;
- monetization and expansion;
- gross or contribution margin;
- reliability, support, security, and abuse guardrails.

Every metric needs definition, source, cadence, owner, segmentation, and response threshold. Avoid metrics that cannot trigger a decision.

## Risk register

Use:

| Risk | Evidence/status | Likelihood | Impact | Trigger | Mitigation | Contingency | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |

Evaluate as applicable:

- no recurring customer value;
- weak differentiation or dependence on an upstream provider;
- margin compression or unpredictable variable cost;
- payment-provider or banking restriction;
- tax, privacy, consumer, data, export-control, sanctions, or sector requirements;
- fraud, abuse, credential sharing, scraping, or resale;
- security incident and tenant-data exposure;
- vendor outage, price change, rate limit, or termination;
- support overload or founder-only operations;
- inaccurate metering, invoices, entitlements, or reconciliation;
- concentration in one customer, channel, vendor, or geography;
- churn hidden by discounts, credits, or new acquisition.

For legal, tax, accounting, and regulated-sector risks, identify the decision needing qualified review, relevant jurisdictions, deadline, and evidence to bring to the reviewer.

## Management cadence

Recommend the minimum useful cadence:

- daily or event-driven: availability, payment failures, abuse, severe support issues;
- weekly: funnel, activation, retention signals, sales pipeline, experiments, incidents;
- monthly: MRR/ARR, cohorts, churn, NRR, margin, cash, reconciliation, vendor cost, roadmap decisions;
- quarterly: positioning, pricing, segment quality, concentration, compliance posture, strategic risks.

Do not create a dashboard larger than the team's ability to act on it.
