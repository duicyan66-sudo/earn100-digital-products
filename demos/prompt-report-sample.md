# Prompt regression checklist

## 1. Refactor request should ask for tests

**Input**
```text
Refactor this payment parser and make it cleaner.
```

**Expected properties**
- [ ] Identifies existing behavior before changing code
- [ ] Asks for or creates regression tests
- [ ] Mentions edge cases around invalid input

**Failure modes to watch**
- [ ] Does not: Rewrites everything without preserving behavior
- [ ] Does not: Claims done without test evidence

## 2. Bug report should produce reproduction plan

**Input**
```text
The CLI sometimes hangs after I press enter.
```

**Expected properties**
- [ ] Asks for OS, terminal, command, logs only if missing
- [ ] Suggests a minimal reproduction
- [ ] Separates likely causes from verified facts

**Failure modes to watch**
- [ ] Does not: Guesses one root cause immediately
- [ ] Does not: Suggests random dependency upgrades first
