# Product and platform readiness

Read this reference when translating the commercial offer into SaaS product and platform requirements.

## Commercial capability map

For every paid promise, map:

`Offer → Entitlement → Product behavior → Meter/event → Billing state → Customer visibility → Support/admin action`

If any link is missing, the offer is not operationally complete.

## Launch-blocking foundations

Choose only what the product actually needs, but explicitly evaluate:

- account creation, authentication, recovery, verification, and deletion;
- tenant or workspace model and data isolation;
- roles, ownership transfer, invitations, and least privilege;
- onboarding path to first value;
- plan catalog, entitlements, limits, quotas, and feature flags;
- usage metering and immutable billable-event identity;
- subscription and billing state synchronization;
- upgrade, downgrade, cancellation, grace-period, and reactivation behavior;
- receipts, invoices, payment history, and self-service billing management;
- transactional email and notification preferences;
- product analytics for activation and retention;
- internal admin tools with audited access;
- support, status, incident communication, and account diagnostics;
- backups, restore tests, export, retention, and deletion;
- logs, metrics, traces, alerts, and service-level objectives;
- secrets, dependency, vulnerability, and abuse controls.

## Data flow and classification

Map the data path from customer input through the product, infrastructure, vendors, support systems, analytics, logs, backups, and deletion. Classify credentials, billing data, identity data, customer content, telemetry, and derived data separately.

For each class record:

- purpose and lawful or contractual basis where relevant;
- system of record and subprocessors;
- tenant boundary and access roles;
- encryption and secret-handling requirements;
- log redaction and support visibility;
- retention and deletion behavior;
- export and incident-notification implications.

Do not assume application logs are harmless telemetry; they may contain customer content, credentials, identifiers, or regulated data.

## Tenancy decision

Do not default to complex multi-tenancy. Choose from:

- single-user accounts;
- shared workspaces with role-based access;
- logical tenant isolation in a shared application/database;
- stronger database or infrastructure isolation for regulated or high-value tenants.

Document the tenant key, isolation boundary, ownership model, deletion unit, export unit, and audit scope. Verify every data path uses the intended tenant boundary.

## Entitlements and billing state

Maintain a server-side source of truth for access. Payment-provider state alone is not an authorization model.

Define behavior for at least:

- trialing;
- active;
- payment pending;
- past due;
- grace period;
- suspended;
- canceled at period end;
- canceled immediately;
- refunded or disputed;
- manually granted access.

Make webhook processing idempotent and replayable. Record provider event ID, internal event ID, received time, processed time, outcome, and retry history.

## Metering

For usage-based or quota plans, specify:

- metered event and unit;
- event producer and source of truth;
- deduplication key;
- aggregation window and timezone;
- late-arriving event handling;
- corrections and disputes;
- customer-visible usage and alerts;
- hard limit, soft limit, overage, or throttling behavior;
- reconciliation between product usage and invoice line items.

Do not bill from analytics events that can be dropped, reordered, or duplicated without reconciliation.

## Onboarding and activation

Define one activation event that predicts retained value. The onboarding path should minimize time to that event.

Specify:

- empty state and sample data behavior;
- required integrations or credentials;
- progressive disclosure of advanced settings;
- success confirmation;
- abandoned-onboarding recovery;
- human intervention threshold;
- activation telemetry.

## Admin and support tooling

At launch, authorized operators should be able to:

- find a customer and tenant safely;
- inspect plan, entitlement, usage, and billing state;
- view relevant events without exposing secrets;
- resend verification or billing communications;
- apply a documented credit or manual entitlement with expiry;
- suspend abusive accounts;
- export or delete data through audited workflows;
- correlate customer reports with incidents and logs.

Dangerous actions need role restrictions, reason capture, audit logs, and confirmation proportional to risk.

## Reliability targets without history

When the product has no trustworthy baseline, set temporary internal objectives rather than publishing an SLA:

1. Define the customer-visible critical path and the maximum tolerable interruption for the target use case.
2. Measure success rate, latency percentiles, saturation, dependency errors, and recovery time for an initial observation window.
3. Set conservative alert thresholds from customer harm and dependency limits, not arbitrary “five nines” goals.
4. Run failure and restore exercises during the paid pilot.
5. Revise objectives from observed percentiles, incident frequency, support reports, and the cost of further improvement.
6. Publish a contractual commitment only when monitoring, staffing, incident response, exclusions, and remedies can support it.

## Readiness classification

Classify each item:

- **Pilot blocker:** A small, manually supervised paid cohort cannot safely receive and use the promised outcome without it.
- **Public-launch blocker:** Uncontrolled self-service customers cannot safely discover, buy, receive, use, renew, get support for, or leave the service without it.
- **Next:** Materially improves conversion, retention, efficiency, or reliability after initial validation.
- **Scale later:** Needed only after usage, team size, regulation, or enterprise requirements cross a named threshold.

Every recommended capability must include the commercial reason and acceptance evidence.
