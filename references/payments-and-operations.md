# Payments and operating model

Read this reference for checkout, subscriptions, invoicing, tax operations, dunning, refunds, reconciliation, support, and back-office workflows.

## Provider roles

Do not collapse these roles into the word “payments”:

| Role | Responsibility |
| --- | --- |
| Payment processor or PSP | Authorizes and settles payment methods |
| Merchant of record | Acts as seller of record and usually handles indirect tax and chargebacks under its terms |
| Billing engine | Plans, subscriptions, invoices, proration, usage, and billing schedules |
| Tax service | Tax calculation, evidence, registrations, returns, or reporting depending on product |
| Accounting ledger | Financial books, revenue/cash reconciliation, expenses, and reporting |
| Fraud service | Risk signals, rules, authentication, review, and abuse prevention |

A provider may fill several roles, but confirm the contract and current product scope.

## Provider-selection inputs

Verify before recommending a specific provider:

- seller entity country and entity type;
- founder residency constraints when relevant;
- buyer countries and B2B/B2C mix;
- settlement countries, currencies, and bank accounts;
- recurring, usage-based, prepaid-credit, invoice, or marketplace needs;
- average order value and expected volume;
- required payment methods;
- refund and chargeback exposure;
- tax-registration appetite;
- prohibited or restricted business categories;
- data-residency or compliance requirements;
- need for branded checkout, API control, or reseller structure.

Use current primary-source documentation for availability and fees. Do not infer global support from a provider's brand recognition.

Treat these as independent gates:

1. the payment or merchant-of-record provider accepts the seller and business model;
2. the bank or payout rail accepts settlements and expected transaction patterns;
3. upstream vendors, licenses, and platform terms permit the product's resale, aggregation, embedding, or sublicensing model;
4. the planned customer geographies and use cases are permitted.

Keep written evidence and renewal dates where approval can expire or terms can change.

## Order-to-cash map

Document the normal and exception paths:

1. Lead or visitor source
2. Account and identity creation
3. Plan selection or quote
4. Checkout, purchase order, or contract
5. Payment authorization
6. Tax evidence and invoice creation
7. Provisioning and entitlement activation
8. Usage or seat changes
9. Renewal or recurring invoice
10. Failed-payment recovery
11. Upgrade, downgrade, credit, or proration
12. Cancellation and access end
13. Refund or dispute
14. Payout and reconciliation
15. Revenue and management reporting

For each step identify system of record, event, owner, customer communication, retry behavior, and manual recovery route.

## Subscription-state rules

Write explicit answers for:

- When does access begin: authorization, captured payment, signed contract, or manual approval?
- What happens during asynchronous or pending payment?
- How long is the grace period after failure?
- Which retries and customer messages occur?
- Does downgrade happen immediately or next period?
- How are unused credits, prepaid balances, and overages handled?
- What happens after cancellation, refund, or chargeback?
- Which billing exceptions require human approval?

Never delete customer data automatically at the same moment paid access ends unless the retention policy and customer notice support it.

## Credits, prepaid balances, and currency

If the product sells credits or prepaid usage, distinguish:

- purchased customer balance;
- promotional or bonus balance;
- subscription-included allowance;
- refundable balance;
- expired or forfeited balance;
- consumed usage and recognized revenue.

Define consumption order, expiration, transferability, refundability, negative-balance behavior, account closure, chargebacks, and ledger treatment. Confirm the accounting, tax, consumer, and stored-value implications with qualified reviewers where relevant.

For cross-currency sales, define display currency, charge currency, settlement currency, upstream cost currency, exchange-rate source, price-refresh cadence, rounding, conversion fees, reserves, payout delays, and who bears currency movement. Do not hide exchange risk inside a fixed markup.

## Reconciliation

At minimum reconcile:

`Orders/subscriptions ↔ provider charges ↔ refunds/disputes ↔ payouts/fees ↔ bank deposits ↔ accounting records`

Define cadence, owner, acceptable variance, unmatched-item queue, evidence retention, and close procedure. Gross payment volume is not revenue, and provider balance is not cash in the bank.

## Support operating model

Define:

- support channels by plan;
- hours and response targets;
- severity levels and escalation;
- identity verification before account changes;
- billing, abuse, security, and privacy escalation paths;
- incident communication owner;
- refund authority and exception log;
- support data access boundaries;
- knowledge-base ownership and update cadence.

Do not promise 24/7 support without staffing or a realistic on-call model.

## Manual-first operations

Manual work is acceptable at launch when volume is low and the action is reversible, auditable, and documented. For every manual workflow specify:

- operator and backup;
- trigger and expected frequency;
- checklist and permissions;
- audit evidence;
- failure recovery;
- automation threshold based on volume, latency, error rate, or risk.

## Existing-customer migration

When customers already exist, specify:

- account and tenant mapping;
- balance and usage-ledger import with before/after reconciliation;
- grandfathered price, entitlement, and expiry rules;
- billing-date and payment-method migration;
- consent or acceptance of updated terms and policies;
- customer communications and support coverage;
- dual-run, cutover, rollback, and dispute handling;
- final sign-off evidence for each migrated cohort.

## Policy surface

Identify the need for terms, privacy notice, acceptable-use policy, refund/cancellation terms, service levels, data-processing terms, subprocessor disclosure, cookie notice, and sector-specific notices. Match policies to real product behavior. Do not fabricate legal text or claim compliance based only on publishing documents.
