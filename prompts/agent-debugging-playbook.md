# Agent debugging playbook

A practical prompt for debugging flaky AI-agent workflows.

```text
You are debugging an AI agent failure. Do not patch first.

Phase 1: Reconstruct
- What was the user trying to accomplish?
- What tools/actions were actually used?
- Where did observed behavior diverge from expected behavior?

Phase 2: Localize
- Is this model reasoning, tool schema, auth, environment, state, network, or UI?
- What is the smallest reproduction?

Phase 3: Fix
- Propose the smallest change that addresses the root cause.
- Identify any side effects.

Phase 4: Verify
- Give exact commands/tests.
- State what output would prove the fix worked.
```
