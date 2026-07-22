# Working With an Agent

A portable operating guide for turning an LLM from an agreeable answer machine into a correctable, tool-using collaborator.

The system is larger than a standing prompt:

- a **working agreement** governs posture and judgment;
- **memory** stores durable facts, not task debris;
- **skills** store reusable methods;
- **task context** carries immediate goals and constraints;
- **tools** let the agent inspect and act;
- **approval boundaries** govern autonomy;
- **verification** separates attempted work from completed work.

## Start here

- `guide/OPERATING-GUIDE.md` — the model
- `templates/working-agreement.md` — copyable compact contract
- `templates/autonomy-budget.md` — reversibility and external-impact matrix
- `SKILL.md` — portable agent skill

Audit a customized agreement before sharing it:

```bash
python3 scripts/audit_agreement.py templates/working-agreement.md
python3 -m unittest discover -s tests -v
```

The audit is conservative and intentionally catches common credentials, private network details, and missing operating clauses. It is not a substitute for human review.

MIT licensed.
