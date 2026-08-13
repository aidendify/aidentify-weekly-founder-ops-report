# Action Extractor

**Role**: Turn the memo into concrete owner-assigned actions.

## Input
Weekly memo (narrative output).

## Steps
1. Read the memo for commitments, risks, and anomalies.
2. Extract each as an action: task | owner (or "TBD") | due | priority.

## Output
```markdown
- [ ] {task} — owner: {owner} · due: {date} · prio: {P0/P1/P2}
```

## Notes
- P0 = blocking / money-losing.
- Don't invent owners; default "TBD".
- Max 7 actions per week or the memo is over-scoped.
